import os
import quantstats as qs
#import webbrowser as web
import yfinance as yf
import pandas as pd
import streamlit as st

ticker='2330.TW'
benchmark='0050.TW'
df_ret=yf.download(ticker, period='10y')['Adj Close'].pct_change()
bmk=yf.download(benchmark, period='10y')['Adj Close'].pct_change()
benchmark=pd.Series(data=bmk, index=df_ret.index).fillna(0)
qs.extend_pandas()
qs.plots.snapshot(df_ret, title='Facebook Performance')

import pandas as pd
import requests
id='00779B' #https://github.com/polaryang/streamlit-example/blob/08f2526337ec7dd9ff5e951ffc5c18c543f1f4fc/EFT_Dividend.xlsx
url= 'https://github.com/polaryang/streamlit-example/blob/08f2526337ec7dd9ff5e951ffc5c18c543f1f4fc/EFT_Dividend.xlsx'
url='https://github.com/polaryang/streamlit-example/raw/08f2526337ec7dd9ff5e951ffc5c18c543f1f4fc/EFT_Dividend.xlsx'
myfile = requests.get(url)
#st.write(myfile.text)
df = pd.read_excel(url)
df1=df[df['代碼']==id]
print(df1)
years=['2018', '2019', '2020', '2021', '2022']
divid_list=[]
for i in range(8,3,-1):
    #print(i)
    divid_list.append(df1.iloc[0, i])
df_etf=pd.DataFrame(divid_list, index = years, columns =['Dividends'])
df_etf=df_etf.dropna()
st.dataframe(df_etf)
