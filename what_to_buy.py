from extra import *
from helpers import *
from constants import *
import json
import pandas as pd

# 8 41.538231 1731.047834  4.55  ([25, 81], -12)

columns = ['ticker', 'prev_date','prev_price', 'latest_price','percentage_diff', 'fall_window','fall_percentage']
price_key = 'adj_close'
"""
for each stock
check change between latest price and price of 25 days ago
if change is less than or equal to -12,
add to DF
DF should have ticker, prev price, current price, fall_percentage
"""
fall_windows = [i for i in range(20,50)]
fall_percentages = [i for i in range(-40, -10)]


with open('indian_stock_data.json') as f:
    stock_data = json.load(f)
to_buy = []
unique_stocks=[]

for fall_window in fall_windows:
    for fall_percentage in fall_percentages:

        for s in stock_data:
            if len(stock_data[s]) > 235:
                ticker_data = stock_data[s]
                prev_row = get_prev_price(ticker_data,fall_window)

                latest_price = get_latest_price(ticker_data)[price_key]
                prev_price = prev_row[price_key]
                percentage_diff = get_percent_change(prev_price,latest_price)

                if percentage_diff <= fall_percentage:
                    prev_date = prev_row['date']
                    if not s in unique_stocks:
                        unique_stocks.append(s)
                        to_buy.append([s,prev_date, prev_price, latest_price, percentage_diff, fall_window, fall_percentage])
to_buy_df = pd.DataFrame(to_buy, columns=columns)
pd.set_option("display.max_rows", None)

if not to_buy_df.empty:
    print(to_buy_df.sort_values('percentage_diff'))
