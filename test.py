import streamlit as st
import yfinance as yf
import datetime
import mpld3
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

d = st.date_input(
     'Starting Date:',
     datetime.date(2018, 1, 1))
st.write('Starting Date:', d)

today = datetime.date.today()
stock_ticker=st.text_input('Input Ticker','2330.TW')
data_h = yf.download(stock_ticker, start=d, end=today, interval="1d")

option = st.selectbox(
     'What kind of information you want to see?',
     ('Stock Price', 'Return(%)'))
st.write('You selected:', option)

y=data_h.Close
x=data_h.index
if option == 'Return(%)':
     data_r = data_h.pct_change()
     y=data_r.Close*100
     x=data_r.index

#create figure
fig=plt.figure()
plt.plot(x,y,linestyle='-',color='b')
plt.title('Stock '+stock_ticker+' '+option)
#rotate x-axis tick labels
plt.xticks(rotation=45, ha='right')
#st.pyplot(fig)
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)

print(data_h.Close)
st.dataframe(data_h)
