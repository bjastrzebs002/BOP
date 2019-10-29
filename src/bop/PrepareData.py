from datetime import datetime


def prepare(unsorted_list):
    r = unsorted_list[0]['rates']
    dates_n_rates = []
    for key, val in r.items():
        temp_tuple = tuple((datetime.strptime(key, '%Y-%m-%d').date(), val['USD']))
        dates_n_rates.append(temp_tuple)
    sort_d(dates_n_rates)
    return dates_n_rates


def sort_d(dates_n_rates):
    dates_n_rates.sort(key=lambda date: date[0])

