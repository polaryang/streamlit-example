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
     'your birthday',
     datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

today = datetime.date.today()
stock_ticker='2330.TW'
data_h = yf.download(stock_ticker, start="2018-05-18", end=today, interval="1d")
print(data_h.Close)
st.dataframe(data_h)

#create figure
fig=plt.figure()
y=data_h.Close
x=data_h.index
plt.plot(x,y,linestyle='-',color='b')
plt.title('Stock Price')
#rotate x-axis tick labels
plt.xticks(rotation=45, ha='right')
#st.pyplot(fig)
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)

