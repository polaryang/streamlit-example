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

import requests
from bs4 import BeautifulSoup
import pandas as pd
# https://statementdog.com/screeners/dividend_yield_ranking
# https://statementdog.com/blog/archives/10896
# https://tw.stock.yahoo.com/tw-etf/yield
r = requests.get("https://statementdog.com/screeners/dividend_yield_ranking")
soup = BeautifulSoup(r.text, 'html.parser')
id_code=[]
id_name=[]
stories1 = soup.find_all("li", {"class":"ranking-item-info ranking-item-ticker-name"})
for i in range(1,len(stories1)):
        [code,name]=stories1[i].text.split()
        id_code.append(code)    
        id_name.append(name)  
stories2 = soup.find_all("li", {"class":"ranking-item-info ranking-item-dividend-yield is-sorted"})
rank1y=[]
for i in range(1,len(stories2)):
       rank1y.append(float(stories2[i].text.replace('%','')))   
stories3 = soup.find_all("li", {"class":"ranking-item-info ranking-item-dividend-yield-3Y"})
rank3y=[]
for i in range(1,len(stories3)):
       rank3y.append(float(stories3[i].text.replace('%',''))) 
df_ranking=pd.DataFrame({'id_code':id_code,'id_name':id_name, 'rank1y':rank1y, 'rank3y':rank3y})
df_ranking=df_ranking.sort_values(by='rank3y',ascending=False,ignore_index=True)
all_list=[]
for i in range(len(df_ranking)):
    spaces='  '*(7-len(df_ranking['id_name'][i]))
    all_list.append(df_ranking['id_code'][i]+'  '+df_ranking['id_name'][i]+spaces+str(df_ranking['rank3y'][i])+'%')
st.dataframe(df_ranking)

check_yes=st.checkbox("Enable selectbox widget")
option_input=st.text_input('stock?','2303',disabled=check_yes)
option_select = st.selectbox(
"How would you like to be contacted?",
all_list, disabled=not check_yes, )
option_select.split()
if check_yes:
   option= option_select   
else:
   option= option_input
st.write(option)

