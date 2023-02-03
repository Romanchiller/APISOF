import requests
from pprint import pprint
from datetime import date, timedelta
import time


def get_questions(day_1,day_2):
    URL = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': day_1,
              'todate': day_2,
              'order': 'desc',
              'site': 'stackoverflow',
              'tagged': 'Python',
              'sort': 'activity'
              }
    response = requests.get(url=URL, params=params)
    return pprint(response.json())


if __name__ == '__main__':
    today = date.today()
    yesterday = date.today() - timedelta(days=1)
    unixtime_today = time.mktime(date.today().timetuple())
    unixtime_yesterday = time.mktime((date.today() - timedelta(days=1)).timetuple())

    get_questions(int(unixtime_yesterday), int(unixtime_today))

