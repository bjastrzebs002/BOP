from datetime import datetime
from datetime import timedelta
from RequestHandler import RequestHandler


lista = RequestHandler().get_data()


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
                temp_tuple = tuple((datetime.strptime(key, '%Y-%m-%d').date(), val['EUR']))
                dates_n_rates.append(temp_tuple)
            self.sort_d(dates_n_rates)
            self.add_missing_d(dates_n_rates)
            self.all_dates.append(dates_n_rates)
            #print(dates_n_rates[-1][1])
            #print(dates_n_rates[-2][1])
            self.results.append(self.compare(dates_n_rates))
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
        if len(dates_n_rates) > 101:
            for x in range(len(dates_n_rates) - 101):
                dates_n_rates.pop(0)
        elif len(dates_n_rates) < 101:
            for x in range(len(dates_n_rates)):
                temp_data = dates_n_rates[0]
                dates_n_rates.append(temp_data)

    def compare(self, dates_n_rates):
        if dates_n_rates[-1][1] > dates_n_rates[-2][1]:
            return 1
        else:
            return 0


#print(lista)
A = PrepareData(lista)
A.prepare()
#print(A.all_dates[0][0][1])
#print(A.all_dates[0][-1])
for x in range(len(A.all_dates)):
    print(len(A.all_dates[x]))
print(A.results)