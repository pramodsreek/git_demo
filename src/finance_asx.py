'''
This modules checks the stock price for buy or sell recommendation.
'''

import datetime as dt
from matplotlib import style
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
#from mpl_finance import candlestick_ohlc
import pandas as pd
import pandas_datareader.data as web
from yahoo_finance import share


START = dt.datetime(2018, 1, 1)
END = dt.datetime(2019, 6, 19)

DF = web.DataReader('ANZ.AX', 'yahoo', START, END)
##print(DF.head(6))
print(DF.tail(6))


print (web.YahooDailyReader('ANZ.AX'))
# get live price of Apple
yahoo = Share('YHOO')



DF.to_csv('anz.csv')

DF = pd.read_csv('anz.csv', parse_dates=True, index_col=0)

DF['100ma'] = DF['Adj Close'].rolling(window=100).mean()
DF.dropna(inplace=True)

print(DF.head())


