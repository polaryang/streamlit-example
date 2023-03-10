import streamlit as st
import yfinance as yf
import datetime
st.write("hello world")
today = datetime.date.today()
stock_ticker='2330.TW'
data_h = yf.download(stock_ticker, start="2018-05-18", end=today, interval="1d")
print(data_h.Close)
import matplotlib.pyplot as plt

#create figure
plt.figure()
y=data_h.Close
x=data_h.index
plt.plot(x,y,linestyle=':',color='b',marker='*')
plt.title('Stock Price')
#rotate x-axis tick labels
plt.xticks(rotation=45, ha='right')

plt.show()
