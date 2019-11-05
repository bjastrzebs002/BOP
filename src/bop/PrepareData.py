from datetime import datetime
from datetime import timedelta

lista = [{"rates":{"2018-09-01":{"USD":0.87},"2018-08-01":{"USD":0.85},"2018-07-30":{"USD":0.84},"2018-09-05":{"USD":0.86}},{"2018-09-01":{"USD":0.87},"2018-08-01":{"USD":0.85},"2018-07-30":{"USD":0.84},"2018-09-05":{"USD":0.86}}]}]


class PrepareData:
    def __init__(self, unsorted_list):
        self.unsorted_list = unsorted_list
        self.all_dates = []
        self.results = []

    def prepare(self):
        for x in self.unsorted_list:
            r = x['rates']
            dates_n_rates = []
            for key, val in r.items():
                temp_tuple = tuple((datetime.strptime(key, '%Y-%m-%d').date(), val['USD']))
                dates_n_rates.append(temp_tuple)
            self.sort_d(dates_n_rates)
            self.add_missing_d(dates_n_rates)
            self.all_dates.append(dates_n_rates)
        return self.all_dates, self.results

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

    def compare(self, dates_n_rates):
        return self.results


A = PrepareData(lista)
print(A.prepare())


