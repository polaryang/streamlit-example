import os
import quantstats as qs
#import webbrowser as web
import yfinance as yf
import pandas as pd

ticker='2330.TW'
benchmark='0050.TW'
df_ret=yf.download(ticker, period='10y')['Adj Close'].pct_change()
bmk=yf.download(benchmark, period='10y')['Adj Close'].pct_change()
benchmark=pd.Series(data=bmk, index=df_ret.index).fillna(0)
qs.extend_pandas()
qs.plots.snapshot(df_ret, title='Facebook Performance')
