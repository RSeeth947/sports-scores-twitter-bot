from bs4 import BeautifulSoup
import requests

url = 'https://www.espn.com/soccer/match/_/gameId/635042'
comment_url = 'https://www.espn.com/soccer/commentary?gameId=635044'

result = requests.get(url)
comment_result = requests.get(comment_url).text

doc = BeautifulSoup(result.text, "html.parser")
comment_doc = BeautifulSoup(comment_result, "html.parser")


class GameInfo:

    def __init__(self, url):
        self.url = url[0]
        self.comment_url = url[1]
        self.result = requests.get(self.url)
        self.comment_result = requests.get(self.comment_url)
        self.doc = BeautifulSoup(self.result.text, "html.parser")
        self.comment_doc = BeautifulSoup(self.comment_result.text, "html.parser")

    def refresh(self):
        self.result = requests.get(self.url)
        self.doc = BeautifulSoup(self.result.text, "html.parser")

        self.comment_result = requests.get(self.comment_url)
        self.comment.doc = BeautifulSoup(self.comment_result.text, "html.parser")


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

    def post_comments(self, comment_list):
        container = self.comment_doc.find('div', id='match-commentary-1-tab-2')
        comment_data = container.find_all('tr')

        for item in comment_data:
            comment = (item.find('td', class_='time-stamp').text,item.find('td', class_='game-details').string.strip())
            if comment not in comment_list:
                tweet = f"{comment[0]}: {comment[1]}"
                comment_list.append(comment)
                return tweet

        return False







