import streamlit as st
import pandas as pd
st.set_page_config(page_title='桃園埤圳重要濕地（國家級）資料庫', page_icon=':sparkles:', layout='wide')
st.header(':sparkles: 桃園埤圳重要濕地（國家級）資料地圖')
st.header(':yellow[水鳥度冬區] :blue[野生動物保護區] :green[環境教育區] :red[生物多樣性較高]')


#in_file='D:\James\Research\ESG\濕地\TY_Wetlands.xlsx'
in_file='https://github.com/polaryang/streamlit-example/raw/master/TY_Wetlands1.xlsx'
choice_list=['全部', '水鳥度冬區', '野生動物保護區', '野生動物保護區附近', '環境教育區', '環境教育區附近', '生物多樣性較高區']
options = st.multiselect(
    'What are your favorite wetlands', choice_list,['全部'])
st.write('You selected:', options)
df=pd.read_excel(in_file, sheet_name='data')
#for i in range(len(df)):
#    print(df['緯度'][i],df['經度'][i])
st.map(df, latitude='緯度',  longitude='經度', size=100, color='選點原因Color')
print(df)
 
