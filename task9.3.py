import sys
sys.path.append("/usr/lib/python3/dist-packages")
import requests
import datetime

class StackOverflowHandling():
    def __init__(self):
        self.time_now = round(datetime.datetime.timestamp(datetime.datetime.now()))

        self.params = {'fromdate': f'{self.time_now - 2*86400}',
                  'todate': f'{self.time_now}',
                  'tagged': 'Python',
                  'site': 'stackoverflow'
                  }
    def QueryQuestions(self):
        resp = requests.get('https://api.stackexchange.com/questions', params=self.params)
        print(resp.status_code)
        records_list = resp.json().get('items')
        print(records_list)
        for i in records_list:
            print(f'\nTITLE\n{i.get("title")}')


so = StackOverflowHandling()
so.QueryQuestions()
