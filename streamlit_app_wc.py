#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
#options.add_argument('--no-sandbox')
#options.add_argument('--window-size=1420,1080')
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
st.write('Testing')
driver = webdriver.Chrome(ChromeDriverManager().install())
