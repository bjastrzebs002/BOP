from datetime import datetime, timedelta
import numpy as np
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class PrepareData:
    def __init__(self, currency):
        self.all_dates = []
        self.results = []
        self.currency = currency

    def prepare(self, unsorted_list):
        logging.info("Preprocessing downloaded data..")
        for x in unsorted_list:
            r = x['rates']
            start_date, end_date = x["start_at"], x["end_at"]
            dates_n_rates = []
            for key, val in r.items():
                temp_tuple = tuple((datetime.strptime(key, '%Y-%m-%d').date(), val[self.currency]))
                dates_n_rates.append(temp_tuple)
            self.sort_d(dates_n_rates)
            self.add_missing_d(dates_n_rates)
            self.check_boundary(start_date, end_date, dates_n_rates)
            dates_save = self.norm_data(np.array([i[1] for i in dates_n_rates]))
            if len(dates_save) != 101:
                continue
            self.all_dates.append(dates_save[:-1])
            self.results.append(self.compare(dates_n_rates))
        return self.all_dates, np.array(self.results)

    def single_dict_prepare(self, one_dict):
        # single dictionary preparing method
        t = one_dict['rates']
        start_date, end_date = one_dict['start_at'], one_dict['end_at']
        one_dict_dates_n_rates = []
        for key, val in t.items():
            temp_tuple = tuple((datetime.strptime(key, '%Y-%m-%d').date(), val[self.currency]))
            one_dict_dates_n_rates.append(temp_tuple)
        self.sort_d(one_dict_dates_n_rates)
        self.add_missing_d(one_dict_dates_n_rates)
        self.check_boundary(start_date, end_date, one_dict_dates_n_rates)
        one_dict_dates_n_rates = self.norm_data(np.array([x[1] for x in one_dict_dates_n_rates]))
        return one_dict_dates_n_rates

    @staticmethod
    def sort_d(dates_n_rates):
        dates_n_rates.sort(key=lambda date: date[0])

    def add_missing_d(self, dates_n_rates):
        try:
            for x in range(len(dates_n_rates)):
                delta = dates_n_rates[x+1][0] - dates_n_rates[x][0]
                if delta > timedelta(days=1):
                    temp_date = dates_n_rates[x][0] + timedelta(days=1)
                    new_data = (temp_date, dates_n_rates[x][1])
                    dates_n_rates.insert(x+1, new_data)
                    self.add_missing_d(dates_n_rates)
        except IndexError:
            pass

    @staticmethod
    def check_boundary(start, end, dates_n_rates):
        start_date = datetime.strptime(start, '%Y-%m-%d').date()
        end_date = datetime.strptime(end, '%Y-%m-%d').date()
        if dates_n_rates[0][0] != start_date:
            value = dates_n_rates[0][1]
            actual_date = dates_n_rates[0][0] - timedelta(days=1)
            while actual_date != start_date:
                dates_n_rates.insert(0, (actual_date, value))
                actual_date -= timedelta(days=1)
            dates_n_rates.insert(0, (actual_date, value))
        if dates_n_rates[-1][0] != end_date:
            value = dates_n_rates[-1][1]
            actual_date = dates_n_rates[-1][0]
            while actual_date != end_date:
                dates_n_rates.append((actual_date, value))
                actual_date += timedelta(days=1)

    @staticmethod
    def compare(dates_n_rates):
        if dates_n_rates[-1][1] >= dates_n_rates[-2][1]:
            return 1
        else:
            return 0

    @staticmethod
    def norm_data(data):
        return (data - np.mean(data))/np.std(data)
