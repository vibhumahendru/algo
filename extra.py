import json
import requests
from statistics import mean
import itertools
from statistics import StatisticsError

api_key = '01ee7bed0803827d7b32cc0038af8e2e'


def get_date_pairs(data):
    returns_list =[]
    try:
        for idx, d in enumerate(data):
            # if (idx + fall_day_length) < len(data):
            if get_percent_change(d[price_key], data[idx + fall_day_length][price_key]) <= fall_percentage:
                fall_start = d[price_key]
                mid = data[idx + fall_day_length][price_key]
                gain_end = data[idx + fall_day_length + gain_day_length][price_key]

                gain_period_change = get_percent_change(mid, gain_end)
                returns_list.append(gain_period_change)
    except IndexError as e:
        pass
    print(len(returns_list), "LEN")
    print(mean(returns_list), "mean(returns_list)")
    return mean(returns_list)

def generate_vars_dataset(fall_day_length, gain_day_length, fall_percentage, min_fall_percentage):
    """
    [
        [[1,1],-1],
        [[1,2],-1],
    ]
    """
    fall_gap = [i for i in range(1,fall_day_length)]
    rise_gap = [i for i in range(1,gain_day_length)]

    test = list(itertools.product(fall_gap, rise_gap))
    list_percentages = [i for i in range(fall_percentage,min_fall_percentage)]
    return list(itertools.product(test, list_percentages))

def get_percent_change(first_number, second_number):
    return ((second_number - first_number)/first_number) * 100

def get_ticker_data(ticker):

    with open('stock_data.json') as f:
        stock_json_file = json.load(f)

    if ticker in stock_json_file:
        data = stock_json_file[ticker]
    else:
        print("FETCHINNGGG")
        r = requests.get(f'http://api.marketstack.com/v1/eod?access_key={api_key}&symbols={ticker}&limit=2000&sort=ASC')
        data =  json.loads(r.content)['data']
    return data
