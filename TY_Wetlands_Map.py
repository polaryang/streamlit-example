import streamlit as st
import pandas as pd
#in_file='D:\James\Research\ESG\濕地\TY_Wetlands.xlsx'
in_file='https://github.com/polaryang/streamlit-example/raw/master/TY_Wetlands1.xlsx'
df=pd.read_excel(in_file)
#for i in range(len(df)):
#    print(df['緯度'][i],df['經度'][i])
st.map(df, latitude='緯度',  longitude='經度')
