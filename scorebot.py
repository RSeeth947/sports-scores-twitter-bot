import tweepy
import time
import configparser
from getscores import *

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']["access_token_secret"]


auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)


url = ['ESPN Sports Game', 'ESPN Key Events Section']
game = GameInfo(url)


scores = []
comment_list = []

while game.gametime() != "FT":
    game.refresh()
    game_text = f"{game.gametime()}: {game.hometeam()} {game.homescore()} - {game.awayscore()} {game.awayteam()}"
    print("Not yet FT, loop will continue")
    #if gametime == "HT":
        #break
    current_score = (game.homescore(), game.awayscore())
    if game.score_change(scores, current_score):
        scores.append(current_score)
        api.update_status(game_text)
        print("a tweet has been posted")

    if game.get_comment() not in comment_list:
        comment = game.get_comment()
        api.update_status(comment)
        print(comment)
        comment_list.append(comment)

    time.sleep(60)

game.refresh()

end_text = f"FT: {game.hometeam()} {game.homescore()} - {game.awayscore()} {game.awayteam()}"
api.update_status(end_text)
print("Game is over")

