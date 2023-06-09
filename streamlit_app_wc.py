from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
ID='2330'
url = "https://www.cmoney.tw/etf/tw/"+str(ID) #new moudle using pyppeteer
url='https://www.cmoney.tw/etf/tw/'+str(ID)+'/intro'
#title='追蹤指數 ETF類型 管理費(%) 保管費(%) 申購手續費(%) 買回手續費(%) 資料日期'
opt = webdriver.ChromeOptions()
opt.headless = True
chromedriver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# C:\Program Files (x86)\Google\Chrome\Application
# https://github.com/polaryang/streamlit-example/blob/886d0c51c8668fbee9fa1a4a7efdceba7b764908/test1.py
driver = webdriver.Chrome(executable_path=chromedriver, options=opt)
driver.get(url)

#//*[@id="__layout"]/div/div[3]/div/div[2]/main/div/div[3]/div/div/table/tbody/tr[3]/td[1]
#//*[@id="__layout"]/div/div[3]/div/div[2]/main/div/div[3]/div/div/table/tbody/tr[4]/td[1]
#//*[@id="__layout"]/div/div[3]/div/div[2]/main/div/div[3]/div/div/table/tbody/tr[6]/td[2]
#//*[@id="__layout"]/div/div[3]/div/div[2]/main/div/div[3]/div/div/table/tbody/tr[7]/td[1]
#//*[@id="__layout"]/div/div[3]/div/div[2]/main/div/div[3]/div/div/table/tbody/tr[3]/td[2]
track_index=driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div/div[2]/main/div/div[3]/div/div/table/tbody/tr[3]/td[1]').text
etf_type=driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div/div[2]/main/div/div[3]/div/div/table/tbody/tr[4]/td[1]').text
manage_fee=driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div/div[2]/main/div/div[3]/div/div/table/tbody/tr[6]/td[2]').text
cust_fee=driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div/div[2]/main/div/div[3]/div/div/table/tbody/tr[7]/td[1]').text
tracking_method=driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div/div[2]/main/div/div[3]/div/div/table/tbody/tr[3]/td[2]').text
etf_type=etf_type+' '+tracking_method
apply_fee=0
redeem_fee=0
date_price=0
