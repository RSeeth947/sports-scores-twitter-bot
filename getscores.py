from bs4 import BeautifulSoup
import requests

url = 'https://www.espn.com/soccer/match/_/gameId/635042'

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")


class GameInfo:

    def __init__(self, url):
        self.url = url
        self.result = requests.get(url)
        self.doc = BeautifulSoup(self.result.text, "html.parser")

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

    
x = doc.find_all('div', class_='content')
