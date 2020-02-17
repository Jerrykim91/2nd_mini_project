# selenium01_02.py
# 드라이버 팩 다운로드 경로 
# https://chromedriver.chromium.org/downloads

# pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')

# 드라이버 가지고 오기 
driver = webdriver.Chrome('./data/chromedriver.exe', chrome_options= options)

# 드라이버에 진입할 경로 전달
driver.get("https://www.kamis.or.kr/customer/price/retail/period.do?action=daily")


driver.execute_script("document.getElementsByName('email')[0].value='20191216'")
driver.execute_script("document.getElementsByName('pw')[0].value='20191216'")
driver.execute_script("document.getElementsByClassName('btn btn-primary')[0].click()")


# pop창 띄우기 
time.sleep(3)
driver.execute_script('alert("hello")')

