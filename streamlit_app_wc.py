from selenium.webdriver import Chrome
from selenium import webdriver   
#ChromeDriverManager(path = r".\\Drivers").install()
#https://github.com/polaryang/streamlit-example/blob/886d0c51c8668fbee9fa1a4a7efdceba7b764908/test1.py
options=webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1420,1080')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
chromedriver="//github.com/polaryang/streamlit-example/blob/886d0c51c8668fbee9fa1a4a7efdceba7b764908/chromedriver"
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path=chromedriver, options=options)
driver = webdriver.Chrome(chromedriver)
