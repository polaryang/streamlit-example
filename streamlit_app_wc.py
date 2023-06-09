import streamlit as st
import os
import pathlib
from os import listdir
from os.path import isfile, join
st.write("""
# Demo
""")
parent_path = pathlib.Path(__file__).parent.parent.resolve()
data_path = os.path.join(parent_path, "data")
# onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
# option = st.sidebar.selectbox('Pick a dataset', onlyfiles)
# file_location=os.path.join(data_path, option)
# use `file_location` as a parameter to the main script
st.write(data_path)
import pandas as pd
import requests
id='00779B' 
myfile='https://github.com/polaryang/streamlit-example/raw/08f2526337ec7dd9ff5e951ffc5c18c543f1f4fc/EFT_Dividend.xlsx'
df = pd.read_excel(myfile)
df1=df[df['代碼']==id]
print(df1)
years=['2018', '2019', '2020', '2021', '2022']
divid_list=[]
for i in range(8,3,-1):
    #print(i)
    divid_list.append(df1.iloc[0, i])
df_etf=pd.DataFrame(divid_list, index = years, columns =['Dividends'])
df_etf=df_etf.dropna()
st.dataframe(df_etf)
