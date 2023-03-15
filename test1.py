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
import altair as alt

# extend pandas functionality with metrics, etc.
qs.extend_pandas()

st.subheader('_Chung-Jen Yang_  Stock Information Dashboard :sunglasses:')
col1, col2 = st.columns([2,6])
with col1:
  d = st.date_input(
       'Starting Date:',
       datetime.date(2018, 1, 1))
  st.write('Starting Date:', d)
  today = datetime.date.today()
  ticker=st.text_input('Input Ticker','2330.TW')
  benchmark=st.text_input('Input Benchmark','0050.TW')
  
  df = yf.download(ticker, start=d, end=today, interval="1d")
  df_ret=df.pct_change()
  bmk = yf.download(benchmark, start=d, end=today, interval="1d")
  bmk_ret=bmk.pct_change()
  #bmk_ret=bmk_ret.fillna(0,inplace=True)
  df_all = pd.merge(df_ret, bmk_ret, left_index=True, right_index=True)
  df_all['date']=df_all.index

  option = st.selectbox(
       'What information you want to see?',
       ('Stock Price', 'Return(%)'))
  st.write('You selected:', option)
  
y=df.Close
x=df.index
y_b=bmk.Close
x_b=bmk.index
if option == 'Return(%)':
    y=df_ret.Close*100
    x=df_ret.index
    y_b=bmk_ret.Close*100
    x_b=bmk_ret.index
with col2:
  tab1, tab2, tab3 = st.tabs(["Plot", "Data", "Metrics"])
  with tab1:
    #create figure
    #c = alt.Chart(df_all).mark_area().encode(x='date', y=['Close_x', 'Close_y'])
    #st.altair_chart(c, use_container_width=True)

    a = alt.Chart(df_all).mark_area(opacity=1).encode(x='date', y='Close_x')
    b = alt.Chart(df_all).mark_area(opacity=0.6).encode(x='date', y='Close_y')
    c = alt.layer(a, b)
    fig=st.altair_chart(c.resolve_scale(y='independent'), use_container_width=True)

    #fig=plt.figure()
    #plt.plot(x,y,linestyle='-',color='b')
    #plt.title('Stock '+ticker+' '+option)
    #rotate x-axis tick labels
    #plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)
    #fig_html = mpld3.fig_to_html(fig)
    #components.html(fig_html, height=1000, width=1000)
    
  with tab2:
    st.write(ticker)
    st.dataframe(df)
    st.write(benchmark)
    st.dataframe(bmk)
    
  with tab3:
    #fig = qs.plots.snapshot(df_ret.Close, title='Facebook Performance',savefig='sdfs.png')
    matrix = qs.reports.metrics(df_ret.Close,benchmark=bmk_ret.Close,mode='full', display=False)
    st.dataframe(matrix)
    #st.plotly_chart(fig,use_container_width=True)
  
