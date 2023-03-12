import streamlit as st
import yfinance as yf
import datetime
import mpld3
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)
d = st.date_input(
     'Starting Date:',
     datetime.date(2018, 1, 1))
st.write('Starting Date:', d)

today = datetime.date.today()
stock_ticker=st.text_input('Input Ticker','2330.TW')
data_h = yf.download(stock_ticker, start=d, end=today, interval="1d")
data_r = data_h.pct_change()
#create figure
fig=plt.figure()
y=data_r.Close
x=data_r.index
plt.plot(x,y,linestyle='-',color='b')
plt.title('Stock Price')
#rotate x-axis tick labels
plt.xticks(rotation=45, ha='right')
#st.pyplot(fig)
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)

print(data_h.Close)
st.dataframe(data_h)
