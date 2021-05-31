import json
import requests
from statistics import mean
import itertools
from statistics import StatisticsError
import pandas as pd
from extra import *
from constants import *


"""
1. for list of tickers
2.

{
-1:{
values:[
    [[window fall, window gain], occurences, p]
    [[1,1],100,10]],
    [[1,2],80,10]],
    [[1,3],70, 10]],
        ]
    }
}
"""

"""
config
"""

api_key = 'c4031f16b4e3ec0f5610aaddc5a9b4eb'
fall_day_length = 5
gain_day_length = 10


nasdaq_tickers = ['AAPL','MSFT', 'AMZN', 'FB','PEP']
indian_tickers = ['RELIANCE.XNSE', 'TCS.XNSE', 'HDFCBANK.XNSE', 'HINDUNILVR.XNSE', 'HDFC.XNSE', 'ICICIBANK.XNSE', 'INFY.XNSE', 'SBIN.XNSE']

columns = ['Ticker', 'Fall Window', 'Gain Window', 'Fall %', 'occurrences','avg_gain_across_occs', 'total return']

tickers = nasdaq_tickers
price_key = 'adj_close'
fall_percentage = (-20)

day_length = 10

fall_day_length = 4
gain_day_length = 10

min_fall_percentage = -10


def get_mean_returns(ticker, combo_list=[]):
    if len(combo_list):
        combos = combo_list
    else:
        combos = generate_vars_dataset(fall_day_length,gain_day_length,fall_percentage,min_fall_percentage)

    final_set = []
    data = get_ticker_data(ticker)
    for c in combos:
        fall_window = c[0][0]
        gain_window = c[0][1]
        percent = c[1]
        returns_list =[]
        try:
            for idx, d in enumerate(data):
                if len(combo_list):
                    fall_start = d[price_key]
                    mid = data[idx + fall_window][price_key]
                    gain_end = data[idx + fall_window + gain_window][price_key]
                    gain_period_change = get_percent_change(mid, gain_end)
                    returns_list.append(gain_period_change)

                elif get_percent_change(d[price_key], data[idx + fall_window][price_key]) <= percent:
                    fall_start = d[price_key]
                    mid = data[idx + fall_window][price_key]
                    gain_end = data[idx + fall_window + gain_window][price_key]
                    gain_period_change = get_percent_change(mid, gain_end)
                    returns_list.append(gain_period_change)
        except IndexError as e:
            pass
        try:
            occurences = len(returns_list)
            avg_return_per_occurence = mean(returns_list)
            total_return = occurences * avg_return_per_occurence

            final_set.append([fall_window, gain_window, percent, occurences, avg_return_per_occurence, total_return])
        except StatisticsError as e:
            pass

    return final_set


def find_max(tickers, combo_list=[]):

    max_list = []
    for t in tickers:
        max_combo=None
        print("In Find Max - calculating for : ", t)
        max_return = 0
        for d in get_mean_returns(t,combo_list):
            if (d[3] * d[4]) > max_return:
                max_return = (d[3] * d[4])
                max_combo = d
                max_combo.insert(0,t)
        if max_combo:
            max_list.append(max_combo)
    return max_list

def find_change_given_combo(tickers, combo_list=[]):
    change_list = []
    for t in tickers:
        print("calculating for : ", t)
        for d in get_mean_returns(t,combo_list):
            data = d
            data.insert(0,t)
            change_list.append(data)
    return change_list

def get_optimal_combo(tickers):
    max_df = pd.DataFrame(find_max(tickers), columns=columns)
    print("MAX DF")
    print(max_df)
    fall_window = round(max_df["Fall Window"].mean())
    gain_window = round(max_df["Gain Window"].mean())
    fall_percent = max_df["Fall %"].mean()

    combo = [[[fall_window, gain_window],fall_percent]]
    print("OPTIMAL COMBO : ", combo)
    return combo

def run_optimal_combo(tickers):
    optimal = get_optimal_combo(tickers)
    optimal_df = pd.DataFrame(find_change_given_combo(tickers, optimal), columns=columns)
    print("OPTIMAL DF : ")
    print(optimal_df)
    print("-----------------------")
    print("Avg return : ", optimal_df['total return'].mean())
    return optimal_df


run_optimal_combo(nasdaq_stocks)
# run_optimal_combo(['AAPL','MSFT'])


"""

"""








#
