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


url = 'https://www.espn.com/soccer/match/_/gameId/635042'
game = GameInfo(url)


scores = []
game_text = f"{game.gametime()}: {game.hometeam()} {game.homescore()} - {game.awayscore()} {game.awayteam()}"
while game.gametime() != "FT":
    game.refresh()
    print("Not yet FT, loop will continue")
    #if gametime == "HT":
        #break
    current_score = (game.homescore(), game.awayscore())
    if game.score_change(scores, current_score):
        scores.append(current_score)
        #api.update_status(game_text)
        print("a tweet has been posted")

    time.sleep(60)

game.refresh()

end_text = f"FT: {game.hometeam()} {game.homescore()} - {game.awayscore()} {game.awayteam()}"
#api.update_status(end_text)
print("Game is over")

