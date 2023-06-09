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

st.write('Testing')
from webdriver_manager.chrome import ChromeDriverManager
ChromeDriverManager(path = r".\\Drivers").install()
#https://github.com/polaryang/streamlit-example/blob/886d0c51c8668fbee9fa1a4a7efdceba7b764908/test1.py
options=webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1420,1080')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
chromedriver="//github.com/polaryang/streamlit-example/blob/886d0c51c8668fbee9fa1a4a7efdceba7b764908/chromedriver.exe"
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path=chromedriver, options=options)
