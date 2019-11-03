import json
import requests
import matplotlib.pyplot as plt
import numpy as np
import datetime
import random


class RequestHandler:
    def __init__(self):
        self.dates_list = []
        self.DATETIME = datetime.datetime.strptime("2015-01-01", '%Y-%m-%d')

    @staticmethod
    def get_response(start_date, end_date):
        request = "https://api.exchangeratesapi.io/history?start_at=" + start_date + "&end_at=" + end_date + "&symbols=EUR&base=USD"
        r = requests.get(request)
        return json.loads(r.text)

    def get_data(self):
        for i in range(200):
            random_date = (random.randint(-1000, 1000))
            start_date = (self.DATETIME + datetime.timedelta(days=random_date))
            end_date = (start_date + datetime.timedelta(days=101))

            dates = self.get_response(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
            self.dates_list.append(dates)