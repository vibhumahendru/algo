import json
import requests
from statistics import mean
import itertools
from statistics import StatisticsError
import pandas as pd
from extra import *
from constants import *
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cmx
import matplotlib
from matplotlib import cm





"""

for each ticker

- if share falls x percent within y days,
- then calculate gain in z days from fall end

"""
columns = ['ticker', 'fall_window', 'gain_window', 'fall_percentage', 'occurrences','avg_buy_price','avg_gain_across_occs']

fall_day_length = 30
gain_day_length = 100
min_gain_day_length = 10
fall_percentage = -40
min_fall_percentage = -7


def get_gain_after_fall(ticker_data, combo,ticker):
    """
    - get ticker data
    - loop over each to get windows of fall that satisfy percent fall
    - [fall_gap, gain_gap, min_percent_fall, avg_gain_percent, total_gain_percent ]
    """
    price_key = 'adj_close'

    fall_gap = combo[0][0]
    gain_gap = combo[0][1]
    min_fall_percentage = combo[1]
    gain_per_occ =[]
    buy_prices = []
    buy_dates = []
    sell_dates = []
    buy_sell = {
        'buys':[],
        'sells':[],
    }

    try:
        for idx, d in enumerate(ticker_data):
            if get_percent_change(d[price_key], ticker_data[idx + fall_gap][price_key]) <= min_fall_percentage:

                mid = ticker_data[idx + fall_gap][price_key]
                gain_end = ticker_data[idx + fall_gap + gain_gap][price_key]
                gain_period_change = get_percent_change(mid, gain_end)
                gain_per_occ.append(gain_period_change)

                buy_prices.append(mid)
                buy_dates.append(ticker_data[idx + fall_gap]['date'])
                sell_dates.append(ticker_data[idx + fall_gap + gain_gap]['date'])
    except IndexError as e:
        pass

    buy_sell['buys'] = buy_dates
    buy_sell['sells'] = sell_dates
    # print(ticker, "ticker")
    # print(buy_sell, "buy_sell")

    occurences = len(gain_per_occ)
    avg_return_per_occurence = mean(gain_per_occ) if len(gain_per_occ) else 0
    avg_buy_price = mean(buy_prices) if len(buy_prices) else 0
    return [fall_gap, gain_gap, min_fall_percentage, occurences,avg_buy_price, avg_return_per_occurence]


def get_df_given_combos(ticker, ticker_data, combos):
    result_list =[]
    for c in combos:
        gain_info = get_gain_after_fall(ticker_data, c, ticker)
        if gain_info[3]:
            d = gain_info
            d.insert(0, ticker)
            result_list.append(gain_info)
    print(len(result_list), "LEN")
    return result_list



def main_run(tickers, make_graph=False, get_max_info=True):
    combo_set = generate_vars_dataset(fall_day_length, gain_day_length, fall_percentage, min_fall_percentage, min_gain_day_length)
    max_list = []

    for t in tickers:
        ticker_data = get_ticker_data(t)

        combo_results_list = get_df_given_combos(t,ticker_data, combo_set)
        combo_results_df = pd.DataFrame(combo_results_list, columns=columns)
        print(combo_results_df.sort_values('avg_gain_across_occs'))

        try:
            max_row = combo_results_df[combo_results_df['avg_gain_across_occs'] == combo_results_df['avg_gain_across_occs'].max()].to_dict('records')[0]
            max_list.append(max_row)
        except Exception:
            pass


        if make_graph:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            xs = combo_results_df['fall_percentage']
            ys = combo_results_df['fall_window']
            zs = combo_results_df['avg_gain_across_occs']
            ax.scatter(xs, ys, zs, c=zs, cmap="cool", marker='o')
            ax.set_xlabel('fall_percentage')
            ax.set_ylabel('fall_window')
            ax.set_zlabel('avg_gain_across_occs')
            ax.set_title(t)


    if get_max_info:
        max_df = pd.DataFrame(max_list, columns=columns)
        print(max_df['fall_window'].mean(), 'fall_window')
        print(max_df['gain_window'].mean(), 'gain_window')
        print(max_df['fall_percentage'].mean(),'fall_percentage')
        print(max_df['avg_gain_across_occs'].mean(),'avg_gain_across_occs')
        print(max_df, "max_df")

    if make_graph:
        plt.show()


def selected_combo_run(tickers, single_combo):
    concatonated = []
    avg_list = []
    for idx, t in enumerate(tickers):
        print("Remaining tickers : ", len(tickers) - idx )
        ticker_data = get_ticker_data(t)
        concatonated = concatonated + get_df_given_combos(t,ticker_data, single_combo)
    combo_results_df = pd.DataFrame(concatonated, columns=columns)

    avg_gain_across_occs =combo_results_df['avg_gain_across_occs'].mean()
    avg_buy_price =combo_results_df['avg_buy_price'].mean()
    occurrences = combo_results_df['occurrences'].sum()
    print(combo_results_df.sort_values('avg_gain_across_occs'))
    print("avg_gain_across_occs : ", avg_gain_across_occs)
    print("Avg buy price : ", avg_buy_price)
    print("Total occurrences : ", occurrences)
    print([avg_gain_across_occs, avg_buy_price, occurrences, single_combo])
    return [avg_gain_across_occs, avg_buy_price, occurrences, single_combo]
def run():
    # main_run(indian_stocks,make_graph=False)
    avgs_for_all =[]
    for c in combos:
        list_for_combo = []
        for t in indian_stocks:
            temp = selected_combo_run([t], [c])
            temp.append(t)
            list_for_combo.append(temp)
        given_combo_df = pd.DataFrame(list_for_combo, columns=['avg_gain_across_occs','avg_buy_price', 'occurrences', 'single_combo', 'ticker'])
        avgs_for_all.append(
        [given_combo_df['avg_gain_across_occs'].mean(),
        given_combo_df['avg_buy_price'].mean(),
        given_combo_df['occurrences'].mean(),
        c])

    # print(given_combo_df)
    final_df = pd.DataFrame(avgs_for_all, columns=['avg_gain_across_occs','avg_buy_price','occurrences', 'single_combo'])
    print(final_df.sort_values('avg_gain_across_occs'), "final_df")

run()




#INDIAN STOCKS
#mean of max
# 14.1875 fall_window
# 81.29166666666667 gain_window
# -12.354166666666666 fall_percentage
# 61.76219245309744 avg_gain_across_occs

# Avg return :  145.7378891163793 ..... [[[15,30],-7]]
# Avg return :  203.20283030698388 ..... [[[25,30],-7]] #observed through graphs
# Avg return :  173.20283030698388 ..... [[[23,26],-8.15]]

#NASDAQ STOCKS
# mean of max
# 20.18 fall_window
# 24.28 gain_window
# -8.21 fall_percentage
# 184.20958947383804 total_return

#indivdual runs
# Avg return :  132.1307141891033 ..... [[[15,30],-7]] #observed through graphs
# Avg return :  122.05750752403382 ..... [[[25,30],-7]]
# Avg return :  112.87872029548502 ..... [[[20,24],-7]]] # this was avg of max means
