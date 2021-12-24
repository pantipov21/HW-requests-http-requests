import sys
sys.path.append("/usr/lib/python3/dist-packages")
import requests


# ВАРИАНТ 1
class hw9_1_case1:
    def __init__(self, heros):
        self.heros = heros
        self.max_intelligence = -1
        self.winner_id = -1
        print("Processing.", end='')


    def get_intelligence(self, id):
        url = "https://superheroapi.com/api/2619421814940190/"+str(id)+"/powerstats"
        resp = requests.get(url)
        response = eval(resp.text)
        if int(response.get('intelligence')) > self.max_intelligence:
            self.max_intelligence = int(response.get('intelligence'))
            self.winner_id = id


    def search_ids(self):
        url = "https://superheroapi.com/api/2619421814940190/search/"
        for hero in self.heros:
            resp = requests.get(url + hero)
            #print(resp.text)
            print(".", end='')
            if resp.status_code == 200:
                hero_id = eval(resp.text).get('results')[0].get('id')
                self.get_intelligence(hero_id)


    def report(self):
        url = "https://superheroapi.com/api/2619421814940190/"+str(self.winner_id)+"/biography"
        resp = requests.get(url)
        return eval(resp.text).get('name')


# ВАРИАНТ 2
class hw9_1_case2:
    def __init__(self, heros):
        self.heros = heros
        self.max_intelligence = -1
        self.winner_id = -1
        self.winner_name = ""
        print("Processing.", end='')


    def get_most_clever(self):
        url = "https://superheroapi.com/api/2619421814940190/search/"
        for hero in self.heros:
            resp = requests.get(url + hero)
            print(".", end='')
            if resp.status_code == 200:
                response = eval(resp.text)
                #print(response)
                li = response.get('results')
                i = int(li[0].get('powerstats').get('intelligence'))
                if i > self.max_intelligence:
                    self.max_intelligence = i
                    self.winner_id = int(li[0].get('id'))
                    self.winner_name = li[0].get('name')
        return self.winner_name



print("\nC A S E  1")
hw = hw9_1_case1(["Hulk", "Captain America", "Thanos"])
hw.search_ids()
print(f'\nMost clever hero is {hw.report()}')

print("\nC A S E  2 - faster than case 1")
hw2 = hw9_1_case2(["Hulk", "Captain America", "Thanos"])
print(f'\nMost clever guy is {hw2.get_most_clever()}')