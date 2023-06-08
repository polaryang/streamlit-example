import pandas as pd
import yfinance as yf
import datetime
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as components
import altair as alt
def Checking_ID(ID):
  ID_code='0'
  ID_name='0'
  ID_mkt='0'
  ID_type='0'
  #證交所 checking ID search => https://isin.twse.com.tw/isin/class_main.jsp?owncode=00632R&stockname=&isincode=&market=&issuetype=&industry_code=&Page=1&chklike=Y
  if ID.encode( 'UTF-8' ).isdigit() :    #input data (all numbers)
    r = requests.get("https://isin.twse.com.tw/isin/class_main.jsp?owncode="+ str(ID) +"&stockname=&isincode=&market=&issuetype=&industry_code=&Page=1&chklike=Y")
  elif ID.encode( 'UTF-8' ).isalnum ():  #input data (English and numbers)
    r = requests.get("https://isin.twse.com.tw/isin/class_main.jsp?owncode="+ str(ID) +"&stockname=&isincode=&market=&issuetype=&industry_code=&Page=1&chklike=Y")
  else:                                  #input data (Chinese)
    ID= ID.encode('UTF-8').decode('UTF-8','strict')
    r = requests.get("https://isin.twse.com.tw/isin/class_main.jsp?owncode=&stockname="+ str(ID) +"&isincode=&market=&issuetype=&industry_code=&Page=1&chklike=Y")
  try:
    # Whether the download is successful ?
    if r.status_code == requests.codes.ok :
      # using BeautifulSoup parsing HTML code
      soup = BeautifulSoup(r.text, 'html.parser')
      # using CSS td=_FAFAD2 get data 
      stories = soup.find_all('td', bgcolor="#FAFAD2")
      #頁面編號	國際證券編碼	有價證券代號	有價證券名稱	市場別	有價證券別	產業別	公開發行/上市(櫃)/發行日	CFICode	備註
      #1	TW00000632R5	00632R	元大台灣50反1	上市	ETF		2014/10/31	CEOGDU	
      #parsing all td=_FAFAD2 data and reorganization for return string
      for i in range(0,len(stories),10) :   #((stories[i+5].text == '股票') or (stories[i+5].text == 'ETF'))
              ID_code=stories[i+2].text #code
              ID_name=stories[i+3].text #name
              ID_mkt=stories[i+4].text #market
              ID_type=stories[i+5].text #type
    return ID_code, ID_name, ID_mkt, ID_type
              #return ID_code,ID_name,ID_type    #return ID number
  except:
    no_found=1
    ID_code='0'
    ID_name='0'
    ID_mkt='0'
    ID_type='0'
    return ID_code, ID_name, ID_mkt, ID_type
    #return '0','0','0','0'
# ------------------------------------------------------------------
def divid_cf_calc(age,income_a,income_g,expense_a,inflation,idir,
          divid_rate,last_close,invest_p,divid_live_p,redempt):
  age_list=[]
  income_list=[]
  expense_list=[]
  shares_list=[]
  shares_list=[]
  shares_list1=[]
  shares_all_list=[]
  shares_value_list=[]
  divid_list=[]
  divid_share_list=[]
  cash_divid_list=[]
  cash_redempt_list=[]
  cash_all_list=[]
  net_income_list=[]
  for i in range(invest_p+divid_live_p):
      age_list.append(age+i)
      if i <=invest_p: # 複利投資期間
          income_list.append(income_a*(1+income_g)**i)
      else:            # 財富自由期間
          income_list.append(0)
      expense_list.append(expense_a*(1+inflation)**i)
      d_income=max(income_list[-1]-expense_list[-1],0)
      shares_list1.append(d_income*idir/last_close) # 年初存入股票
      if i==0:
          shares_list.append(d_income*idir/last_close) #第1期年初存入股票 
          divid_list.append(shares_list[i]*divid_rate) # 通常6月配息 單位:股

      else:
          shares_list.append(d_income*idir/last_close+shares_list[i-1]) # 年初存入股票+累進資產    
          divid_list.append(shares_all_list[-1]*divid_rate) # 通常6月配息 單位:股
      
      if i <=invest_p: # 複利投資期間
          
          cash_divid_list.append(0)  # 現金領息為 0
          divid_share_list.append(divid_list[-1]/last_close) # 股息換算股票股數
          shares_all_list.append(shares_list[-1]+divid_share_list[-1])  # 股數轉入累進資產
          cash_redempt_list.append(0)

      else:            # 財富自由期間
          shares_all_list.append(shares_all_list[-1])  # 股數轉入累進資產
          cash_divid_list.append(shares_all_list[i]*divid_rate) # 開始現金領
          divid_share_list.append(0) # 股息領出，就不再換算股票股數
          cash_redempt_list.append(0) # 股票贖回產生的現金
          
          if redempt==1:
            income_shortage=cash_divid_list[-1]-expense_list[-1]
            if income_shortage<0:
              share_redempt=min((income_shortage*-1.01),shares_value_list[-1])/last_close # 股票贖回的股數
              cash_redempt_list[-1]=share_redempt*last_close  # 股票贖回產生的現金
              shares_all_list[-1]=shares_all_list[-1]-share_redempt # 股數轉出 累進資產減少
              cash_divid_list[-1]=shares_all_list[i]*divid_rate # 開始現金領
              
      cash_all_list.append(cash_divid_list[-1]+cash_redempt_list[-1])
      shares_value_list.append(shares_all_list[-1]*last_close)
      net_income_list.append(income_list[-1]-expense_list[-1]+cash_all_list[-1])
  # initialize data of lists.
  data = {'Age':age_list,'Income':income_list,'Expense':expense_list,'Cash_All':cash_all_list,
          'Cash_Dividends':cash_divid_list,'Cash_Redempt':cash_redempt_list,'Share_Value':shares_value_list,
          'Shares':shares_all_list,'Dividends':divid_list,'Net_Income':net_income_list}
  # Create DataFrame
  df = pd.DataFrame(data)   
  return df
# ------------------------------------------------------------------  
st.title('銘傳大學:dove_of_peace:財務金融學系')
st.title(':blue[存股-財富自由-規劃] 實驗室:umbrella_with_rain_drops:')
col1, col2 = st.columns([2,6])
with col1:
  # Basic Parameters
  # 「Discretionary Income」（可調用所得／可運用所得／可花費所得／可花用所得／可調動所得）
  today = datetime.date.today()
  start='2010-01-01'
  end=today
  age = st.slider('How old are you?', 0, 120, 30)
  income=st.number_input('Input monthly income',value=60000,step=5000)
  income_g=st.number_input('Input income growth',value=0.02)
  income_bonus=st.number_input('Input bonus (month)',value=2)
  expense=st.number_input('Input monthly expenditure',value=20000,step=5000)
  inflation=st.number_input('Input inflation rate',value=0.03)
  idir = st.slider('Ratio to invest of income (%)', 0, 100, 80)  # invest dispo income ratio
  idir = idir/100
  invest_p = st.slider('Investment periods (years)', 0, 100, 20)  # 複利投資期間
  divid_live_p = st.slider('Live on dividends periods (years)', 0, 100, 20)  # 財富自由期間
  #redempt=st.number_input('Input whether redempt (1/0)',value=1)
  redempt_yn = st.radio("Whether redempt stocks?", ('Yes', 'No'))
  if redempt_yn == 'Yes':
    st.write('You selected Yes.')
    redempt=1
  else:
    st.write("You select No.")
    redempt=0
    
  #ticker
  ID=st.text_input('Input Ticker','2330')
  ID_code='0'
  ID_name='0'
  ID_mkt='0'
  ID_type='0'
  ID_code, ID_name, ID_mkt, ID_type=Checking_ID(ID) 
  if ID_code=='0':
    stock_ticker=ID
  else:
    stock_ticker=ID_code+'.TW'
  if ID_mkt=='上市 ':
    stock_ticker=ID_code+'.TW'
  if ID_mkt=='上櫃 ':
    stock_ticker=ID_code+'.TWO'
  st.write(ID_name+' : '+stock_ticker)
# ------------------------------------------------------------------
data = yf.Ticker(stock_ticker)
divid=data.dividends
divid=data.dividends
splits=data.splits

income_a=income*(12+income_bonus)
expense_a=expense*12
years=pd.Series(data.dividends.index.year)
divid = pd.DataFrame({'divid':divid.values, 'year':years})
divid_yr0=divid.groupby('year').sum()
divid_yr=divid.groupby('year').sum()
divid_l=len(divid_yr)
divid_yr=divid_yr[divid_yr.index<today.year]
divid_yr=divid_yr[divid_yr.index>today.year-min(divid_l,6)]
avg_divid=round(divid_yr['divid'].mean(),2)
max_divid=round(divid_yr['divid'].max(),2)
min_divid=round(divid_yr['divid'].min(),2)
print(divid_yr)
print(splits)
last_close=data.history()['Close'].tail().mean() # 最近5日平均收盤價
with col2:
  tab1, tab2, tab3, tab4 = st.tabs(["Basic Information", "Best Scenario", "Average Scenario", "Worst Scenario"])
  with tab1:
    st.subheader('Investment in '+ID_name+' : '+stock_ticker)
    st.subheader('Historical Dividends Rate ($ per share) : ')
    st.bar_chart(divid_yr0)
    st.subheader(':vertical_traffic_light: Scenarios Based on Recent 5 Years')
    st.write('   :heart_eyes: Max Dividends Rate ($ per share): '+str(max_divid) )
    st.write('   :neutral_face: Average Dividends ($ per share): '+str(avg_divid) )
    st.write('   :sob: Min Dividends ($ per share): '+str(min_divid) )
    st.subheader('Historical Stock Price')
    st.line_chart(data.history()['Close'])
  with tab2:
    divid_rate=max_divid
    st.subheader(':heart_eyes: Max Dividends Rate ($ per share): '+str(max_divid))
    #st.write('Max Dividends Rate ($ per share): '+str(max_divid) )
    #st.write('Average Dividends Rate ($ per share): '+str(avg_divid) )
    #st.write('Min Dividends Rate ($ per share): '+str(min_divid) )
    df=divid_cf_calc(age,income_a,income_g,expense_a,inflation,idir,
          divid_rate,last_close,invest_p,divid_live_p,redempt)
    i = alt.Chart(df, title='Cash Flow Simulation').mark_line(color="steelblue").encode(
    x='Age', y='Income')
    e = alt.Chart(df).mark_line(color='green').encode(
    x='Age', y='Expense')
    c = alt.Chart(df).mark_line(color="red").encode(
    x='Age', y='Cash_All')
    st.altair_chart((i+e+c), use_container_width=True)
    
    c = alt.Chart(df, title='Net Income over Time').mark_line(color="steelblue").encode(
    x='Age', y='Net_Income')
    st.altair_chart(c, use_container_width=True)
    
    c = alt.Chart(df, title='Number of Shares Holded over Time').mark_bar().encode(
    x='Age', y='Shares')
    st.altair_chart(c, use_container_width=True)
    
    st.dataframe(df)
  with tab3:
    divid_rate=avg_divid
    st.subheader(':neutral_face: Average Dividends Rate ($ per share): '+str(avg_divid))
    #st.write('Max Dividends Rate ($ per share): '+str(max_divid) )
    #st.write('Average Dividends Rate ($ per share): '+str(avg_divid) )
    #st.write('Min Dividends Rate ($ per share): '+str(min_divid) )
    df=divid_cf_calc(age,income_a,income_g,expense_a,inflation,idir,
          divid_rate,last_close,invest_p,divid_live_p,redempt)
    i = alt.Chart(df, title='Cash Flow Simulation').mark_line(color="steelblue").encode(
    x='Age', y='Income')
    e = alt.Chart(df).mark_line(color='green').encode(
    x='Age', y='Expense')
    c = alt.Chart(df).mark_line(color="red").encode(
    x='Age', y='Cash_All')
    st.altair_chart((i+e+c), use_container_width=True)
    
    c = alt.Chart(df, title='Net Income over Time').mark_line(color="steelblue").encode(
    x='Age', y='Net_Income')
    st.altair_chart(c, use_container_width=True)
    
    c = alt.Chart(df, title='Number of Shares Holded over Time').mark_bar().encode(
    x='Age', y='Shares')
    st.altair_chart(c, use_container_width=True)
    
    st.dataframe(df)
  with tab4:
    divid_rate=min_divid
    st.subheader(':sob: Min Dividends Rate ($ per share): '+str(min_divid))
    #st.write('Max Dividends Rate ($ per share): '+str(max_divid) )
    #st.write('Average Dividends Rate ($ per share): '+str(avg_divid) )
    #st.write('Min Dividends Rate ($ per share): '+str(min_divid) )
    df=divid_cf_calc(age,income_a,income_g,expense_a,inflation,idir,
          divid_rate,last_close,invest_p,divid_live_p,redempt)
    deficit=len(df[df[Net_Income]<0])
    if deficit>0
      st.subheader(':face_with_symbols_on_mouth: 財富自由計畫 失敗')
     else:
      st.subheader(':smiling_face_with_smiling_eyes_and_hand_covering_mouth: 財富自由計畫 成功')  
    i = alt.Chart(df, title='Cash Flow Simulation').mark_line(color="steelblue").encode(
    x='Age', y='Income')
    e = alt.Chart(df).mark_line(color='green').encode(
    x='Age', y='Expense')
    c = alt.Chart(df).mark_line(color="red").encode(
    x='Age', y='Cash_All')
    st.altair_chart((i+e+c), use_container_width=True)
    
    c = alt.Chart(df, title='Net Income over Time').mark_line(color="steelblue").encode(
    x='Age', y='Net_Income')
    st.altair_chart(c, use_container_width=True)
        
    c = alt.Chart(df, title='Number of Shares Holded over Time').mark_bar().encode(
    x='Age', y='Shares')
    st.altair_chart(c, use_container_width=True)
    
    st.dataframe(df)
    
plt.bar(df['Age'],df['Shares'])
plt.xlabel('Age')
plt.ylabel('Share(s)')
plt.title('Number of Shares')
plt.grid()
plt.show()
plt.plot(df['Age'],df['Income'], color='blue', linewidth=2, marker='o')
plt.plot(df['Age'],df['Expense'], color='red', linewidth=2, marker='o')
plt.plot(df['Age'],df['Cash_All'], color='green', linewidth=2, marker='o')
plt.legend(['Income','Expense','Cash to Live off'])
plt.xlabel('Age')
plt.ylabel('$')
plt.title('Cash Flow')
plt.grid()
plt.show() 
plt.plot(df['Age'],df['Net_Income'], color='red', linewidth=2, marker='o')
plt.xlabel('Age')
plt.ylabel('$')
plt.grid()
plt.title('Net Wealth')
plt.show() 
plt.plot(df['Age'],df['Share_Value'], color='red', linewidth=2, marker='o')
plt.xlabel('Age')
plt.ylabel('$')
plt.grid()
plt.title('Value of Stocks in Hands')
plt.show()     
