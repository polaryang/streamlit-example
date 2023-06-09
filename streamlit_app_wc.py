#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
#options.add_argument('--no-sandbox')
#options.add_argument('--window-size=1420,1080')
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
import pandas as pd
import yfinance as yf
import datetime
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as components
import altair as alt
import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
st.write('Testing')
options=webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1420,1080')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install())
