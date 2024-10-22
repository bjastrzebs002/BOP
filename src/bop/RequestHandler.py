import json
import requests
import datetime
import random
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class RequestHandler:
    def __init__(self, base, symbols):
        self.dates_list = []
        self.currency_list = ["USD", "EUR", "CAD", "CHF", "GBP", "SEK", "PLN"]
        self.DATETIME = datetime.datetime.strptime("2010-01-01", '%Y-%m-%d')
        self.datetime_now = datetime.datetime.now()
        self.base = base
        self.symbols = symbols

    def get_response(self, start_date, end_date):
        if self.base in self.currency_list:
            if self.symbols in self.currency_list:
                request = "https://api.exchangeratesapi.io/history?start_at=" + start_date + "&end_at=" + end_date + \
                          "&symbols=" + self.symbols + "&base=" + self.base
                r = requests.get(request)
                return json.loads(r.text)
        pass

    def get_data(self):
        logging.info("Downloading data from API..")
        alr_dates = []
        for i in range(3000):
            random_date = (random.randint(-3000, 3000))
            while random_date in alr_dates:
                random_date = (random.randint(-3000, 3000))
            alr_dates.append(random_date)

            start_date = (self.DATETIME + datetime.timedelta(days=random_date))
            end_date = (start_date + datetime.timedelta(days=100))

            dates = self.get_response(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
            self.dates_list.append(dates)
        return self.dates_list

    def get_100daysback_data(self):
        end_date = self.datetime_now
        start_date = (end_date - datetime.timedelta(days=99))
        dates = self.get_response(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
        return dates
