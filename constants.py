from extra import *
from new_indian_stocks import *
import json

indian_stocks = ['RELIANCE.XNSE', 'TCS.XNSE', 'HDFCBANK.XNSE', 'HINDUNILVR.XNSE', 'HDFC.XNSE', 'ICICIBANK.XNSE', 'INFY.XNSE', 'KOTAKBANK.XNSE', 'BHARTIARTL.XNSE', 'BAJFINANCE.XNSE', 'SBIN.XNSE', 'ITC.XNSE', 'AXISBANK.XNSE', 'MARUTI.XNSE', 'ASIANPAINT.XNSE', 'LT.XNSE', 'NESTLEIND.XNSE', 'HCLTECH.XNSE', 'DMART.XNSE', 'BAJAJFINSV.XNSE', 'WIPRO.XNSE', 'ULTRACEMCO.XNSE', 'ONGC.XNSE', 'HDFCLIFE.XNSE', 'TITAN.XNSE', 'COALINDIA.XNSE', 'NTPC.XNSE', 'IOC.XNSE', 'POWERGRID.XNSE', 'BPCL.XNSE', 'SBILIFE.XNSE', 'SUNPHARMA.XNSE', 'DABUR.XNSE', 'SHREECEM.XNSE', 'BAJAJ_AUTO.XNSE', 'PIDILITIND.XNSE', 'INDUSINDBK.XNSE', 'TECHM.XNSE', 'BRITANNIA.XNSE', 'HINDZINC.XNSE', 'ADANIPORTS.XNSE', 'ICICIPRULI.XNSE', 'HDFCAMC.XNSE', 'BANDHANBNK.XNSE', 'GODREJCP.XNSE', 'M_M.XNSE', 'JSWSTEEL.XNSE', 'DIVISLAB.XNSE', 'BERGEPAINT.XNSE', 'ICICIGI.XNSE', 'DLF.XNSE', 'DRREDDY.XNSE', 'MCDOWELL_N.XNSE', 'INDIGO.XNSE', 'SIEMENS.XNSE', 'EICHERMOT.XNSE', 'TATAMOTORS.XNSE', 'GAIL.XNSE', 'GRASIM.XNSE', 'VEDL.XNSE', 'TATASTEEL.XNSE', 'AMBUJACEM.XNSE', 'INFRATEL.XNSE', 'GSKCONS.XNSE', 'HEROMOTOCO.XNSE', 'UPL.XNSE', 'HAVELLS.XNSE', 'BAJAJHLDNG.XNSE', 'MARICO.XNSE', 'BOSCHLTD.XNSE', 'PETRONET.XNSE', 'TORNTPHARM.XNSE', 'PGHH.XNSE', 'EMBASSY.RR.XNSE', 'NMDC.XNSE', 'SRTRANSFIN.XNSE', 'ADANITRANS.XNSE', 'WHIRLPOOL.XNSE', 'IRCTC.XNSE', 'KANSAINER.XNSE', 'CADILAHC.XNSE', 'TRENT.XNSE', 'GODREJPROP.XNSE', 'ACC.XNSE', 'ADANIGREEN.XNSE', 'NAM_INDIA.XNSE', 'CHOLAFIN.XNSE', 'PAGEIND.XNSE', 'ADANIENT.XNSE', 'ABB.XNSE', 'ZEEL.XNSE', 'APOLLOHOSP.XNSE', 'VBL.XNSE', 'RECLTD.XNSE', '3MINDIA.XNSE', 'SRF.XNSE', 'NHPC.XNSE', 'VOLTAS.XNSE', 'OFSS.XNSE', 'HAL.XNSE']

nasdaq_stocks = ['MSFT', 'AAPL', 'AMZN', 'GOOG', 'GOOGL', 'FB', 'VOD', 'INTC', 'CMCSA', 'PEP', 'ADBE', 'CSCO', 'NVDA', 'NFLX', 'TSLA', 'COST', 'PYPL', 'AMGN', 'SNY', 'ASML', 'AVGO', 'TXN', 'CHTR', 'SBUX', 'GILD', 'QCOM', 'TMUS', 'MDLZ', 'FISV', 'CME', 'INTU', 'BKNG', 'ADP', 'ISRG', 'VRTX', 'MU', 'AMD', 'BIIB', 'CSX', 'AMAT', 'EQIX', 'JD', 'REGN', 'ATVI', 'EXC', 'LRCX', 'NTES', 'WBA', 'ADSK', 'ILMN', 'ADI', 'ROST', 'WDAY', 'MAR', 'TEAM', 'MNST', 'XEL', 'CTSH', 'SBAC', 'NXPI', 'BIDU', 'MELI', 'EA', 'KHC', 'ZM', 'EBAY', 'TROW', 'LULU', 'CTAS', 'PAYX', 'SIRI', 'ORLY', 'VRSK', 'CSGP', 'WLTW', 'DXCM', 'KLAC', 'ERIC', 'LBRDK', 'SPLK', 'PCAR', 'LBRDA', 'PDD', 'VRSN', 'CERN', 'IDXX', 'MCHP', 'ANSS', 'SNPS', 'XP', 'ALXN', 'AMTD', 'XLNX', 'FAST', 'CPRT', 'SGEN', 'CDNS', 'MTCH', 'NDAQ', 'FOXA']

sub = ['RELIANCE.XNSE', 'TCS.XNSE', 'HDFCBANK.XNSE', 'HINDUNILVR.XNSE', 'BAJAJ_AUTO.XNSE', 'TATASTEEL.XNSE', 'INDUSINDBK.XNSE']
# sub = ['SBILIFE.XNSE', 'SUNPHARMA.XNSE', 'DABUR.XNSE', 'SHREECEM.XNSE', 'BAJAJ_AUTO.XNSE', 'PIDILITIND.XNSE', 'INDUSINDBK.XNSE']

faang = ['AAPL', 'MSFT', 'FB', 'GOOG', 'GOOGL', 'NFLX', 'AMZN','TSLA', 'TWTR','NVDA']

# new = indian_stocks + nasdaq_stocks

def generate_new_ticker_file():
    data = {}
    for idx, t in enumerate(new_indian):
        print("Remaining tickers : ", len(new_indian) - idx )
        data[t] = get_ticker_data(t,fetch_new=True)


    with open('indian_stock_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# fall_gap = [i for i in range(1,fall_day_length)]
# rise_gap = [i for i in range(min_gain_day_length,gain_day_length)]
#
test = [[15,81]]
list_percentages = [i for i in range(-20,-8)]
combos = list(itertools.product(test, list_percentages))

generate_new_ticker_file()

#INDIAN STOCKS
#     avg_gain_across_occs     single_combo
# 11             32.912937   ([14, 81], -9)
# 10             34.355803  ([14, 81], -10)
# 9              37.636459  ([14, 81], -11)
# 8              41.245094  ([14, 81], -12)
# 7              45.327632  ([14, 81], -13)
# 6              48.898620  ([14, 81], -14)
# 0              52.302817  ([14, 81], -20)
# 1              52.887468  ([14, 81], -19)
# 5              53.309574  ([14, 81], -15)
# 2              54.414962  ([14, 81], -18)
# 3              55.211605  ([14, 81], -17)
# 4              56.331264  ([14, 81], -16) final_df
# (venv) vibhus-mbp:strats vibhumahendru$


#  avg_gain_across_occs  avg_buy_price  occurrences     single_combo
# 11             35.440840    1759.172743         8.25   ([25, 81], -9)
# 10             37.441066    1773.732731         6.76  ([25, 81], -10)
# 7              39.406883    1885.001248         3.55  ([25, 81], -13)
# 6              40.011639    1510.749192         2.94  ([25, 81], -14)
# 9              40.765236    1673.993498         5.57  ([25, 81], -11)
# 8              41.538231    1731.047834         4.55  ([25, 81], -12)
# 5              43.680914    1077.724990         2.35  ([25, 81], -15)
# 4              47.453131    1127.396197         1.81  ([25, 81], -16)
# 1              54.604696     439.746977         0.97  ([25, 81], -19)
# 3              54.819508     447.384453         1.42  ([25, 81], -17)
# 2              56.457310     370.495963         1.18  ([25, 81], -18)
# 0              64.754685     501.756851         0.85  ([25, 81], -20) final_df

# avg_gain_across_occs  avg_buy_price  occurrences     single_combo
# 11             33.209645    1947.664893         5.71   ([15, 81], -9)
# 10             36.283213    1670.156988         4.37  ([15, 81], -10)
# 9              38.922243    1663.669829         3.38  ([15, 81], -11)
# 8              39.963266    1739.387688         2.60  ([15, 81], -12)
# 7              45.070548    1060.639441         1.99  ([15, 81], -13)
# 6              49.935000     789.815100         1.55  ([15, 81], -14)
# 5              51.458310     641.052043         1.26  ([15, 81], -15)
# 4              55.256589     679.443252         1.02  ([15, 81], -16)
# 0              56.224415     487.156572         0.53  ([15, 81], -20)
# 3              57.163689     506.627192         0.81  ([15, 81], -17)
# 1              60.983558     460.374610         0.58  ([15, 81], -19)
# 2              64.318234     558.917844         0.66  ([15, 81], -18) final_df



#
