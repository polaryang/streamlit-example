import streamlit as st
import yfinance as yf
import datetime
import mpld3
import streamlit.components.v1 as components

st.write("hello world!!")
today = datetime.date.today()
stock_ticker='2330.TW'
data_h = yf.download(stock_ticker, start="2018-05-18", end=today, interval="1d")
print(data_h.Close)
import matplotlib.pyplot as plt

#create figure
fig=plt.figure()
y=data_h.Close
x=data_h.index
plt.plot(x,y,linestyle=':',color='b',marker='*')
plt.title('Stock Price')
#rotate x-axis tick labels
plt.xticks(rotation=45, ha='right')
＃st.pyplot(fig)
＃plt.show()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
