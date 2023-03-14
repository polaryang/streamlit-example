import streamlit as st
import yfinance as yf
import datetime
import mpld3
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import os
import quantstats as qs
#import webbrowser as web
import pandas as pd

st.subheader('_Chung-Jen Yang_  Stock Information Dashboard :sunglasses:')
col1, col2 = st.columns([2,5])
with col1:
  d = st.date_input(
       'Starting Date:',
       datetime.date(2018, 1, 1))
  st.write('Starting Date:', d)
  today = datetime.date.today()
  ticker=st.text_input('Input Ticker','2330.TW')
  benchmark=st.text_input('Input Ticker','0050.TW')
  
  df = yf.download(ticker, start=d, end=today, interval="1d")
  df_ret=df.pct_change()
  bmk = yf.download(benchmark, start=d, end=today, interval="1d")
  bmk_ret=bmk.pct_change()
  #data=pd.Series(data=bmk_ret, index=bmk_ret.index).fillna(0)
  
  option = st.selectbox(
       'What information you want to see?',
       ('Stock Price', 'Return(%)'))
  st.write('You selected:', option)
  
qs.extend_pandas()
st.qs.plots.snapshot(df_ret, title='Stock')

y=df.Close
x=df.index
if option == 'Return(%)':
     data_r = data_h.pct_change()
     y=df_ret.Close*100
     x=df_ret.index
with col2:
  tab1, tab2 = st.tabs(["Plot", "Data"])
  with tab1:
    #create figure
    fig=plt.figure()
    plt.plot(x,y,linestyle='-',color='b')
    plt.title('Stock '+ticker+' '+option)
    #rotate x-axis tick labels
    plt.xticks(rotation=45, ha='right')
    #st.pyplot(fig)
    fig_html = mpld3.fig_to_html(fig)
    components.html(fig_html, height=600)
  with tab2:
    st.dataframe(df)
