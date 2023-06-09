# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import streamlit as st

# create a screenshot of the webpage
@st.cache
    ID='0050'
    url = "https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID="+str(ID) #new moudle using pyppeteer
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    n = 5
    item_count = 0
    max_length = d_length
    t_year=0
    finalList=' 年度 '+' 股利 '+'殖利率(%)'+' 填息日數 '
    # year 現金股利 股票股利 填息花費日數 年均	年均殖利率(%) 
    while True:  
        d_year=driver.find_element_by_xpath('//*[@id="divDetail"]/table/tbody/tr['+str(n)+']/td[1]').text
        cash_dividend=driver.find_element_by_xpath('//*[@id="divDetail"]/table/tbody/tr['+str(n)+']/td[4]').text
        stock_dividend=driver.find_element_by_xpath('//*[@id="divDetail"]/table/tbody/tr['+str(n)+']/td[7]').text
        payback_days=driver.find_element_by_xpath('//*[@id="divDetail"]/table/tbody/tr['+str(n)+']/td[11]').text
        #avg_price=driver.find_element_by_xpath('//*[@id="divDetail"]/table/tbody/tr['+str(n)+']/td[16]').text
        dividend_yield=driver.find_element_by_xpath('//*[@id="divDetail"]/table/tbody/tr['+str(n)+']/td[19]').text
        #print(d_year, cash_dividend,stock_dividend,dividend_yield,payback_days)
        if d_year=='累計' or item_count>=max_length:
            break
        else:
            n+=1
            item_count+=1    
            if str(d_year)!='∟':
                t_year==d_year
                len(cash_dividend)
                finalList+='\n' + ' ' + d_year+' '+l_fit(cash_dividend)+' '+l_fit(dividend_yield)+' '+ r_fit(payback_days)
    #print(d_year, cash_dividend,stock_dividend,payback_days,avg_price,dividend_yield) 
    #return finalList,item_count
    st.write(d_year, cash_dividend,stock_dividend)



