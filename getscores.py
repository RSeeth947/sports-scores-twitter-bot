from bs4 import BeautifulSoup
import requests

url = 'https://www.espn.com/soccer/match/_/gameId/635042'
mls_url = 'https://www.mlssoccer.com/competitions/u-s-open-cup/2022/matches/lavssac-06-21-2022/feed'

result = requests.get(url)
mls_result = requests.get(mls_url).text

doc = BeautifulSoup(result.text, "html.parser")
mls_doc = BeautifulSoup(mls_result, "html.parser")


class GameInfo:

    def __init__(self, url):
        self.url = url
        self.comment_url = url[1]
        self.result = requests.get(self.url)
        self.comment_results = requests.get(self.comment_url)
        self.doc = BeautifulSoup(self.result.text, "html.parser")
        self.comment_doc = BeautifulSoup(self.comment_results.text, "html.parser")

    def refresh(self):
        self.result = requests.get(self.url)
        self.doc = BeautifulSoup(self.result.text, "html.parser")


    def score_change(scores, current_score):
        if current_score not in scores:
            return True
        
        return False

    def gametime(self):
        gametime = self.doc.find('span', class_="game-time").string

        return gametime

    def hometeam(self):
        teamname = self.doc.find_all('span', class_='team-name')
        hometeam = teamname[0].text
        
        return hometeam

    def awayteam(self):
        teamname = self.doc.find_all('span', class_='team-name')
        awayteam = teamname[1].text
        
        return awayteam

    def homescore(self):
        homescore = self.doc.find('span', class_="score icon-font-after").text.strip()
        return homescore

    def awayscore(self):
        awayscore = self.doc.find('span', class_="score icon-font-before").text.strip()
        return awayscore

    def post_comments(self):
        pass

 
x = doc.find_all(class_="mls-o-match-feed__comment")
print(x)


