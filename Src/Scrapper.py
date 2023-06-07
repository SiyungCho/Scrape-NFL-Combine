#C:\Users\siyun\Downloads\WebScrappingBets\.venv\Scripts\python.exe
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests

import pandas as pd

import player

path = Service("C:\\Users\\siyun\\Downloads\\chromedriver_win32\\chromedriver.exe")
NFL_url = 'https://nflcombineresults.com/nflcombinedata.php?'

driver = webdriver.Chrome(service=path)
driver.get(NFL_url)

data = driver.find_elements(By.TAG_NAME, "tbody")
headers = driver.find_elements(By.TAG_NAME, "thead")

for element in headers:
    text = element.text
    #print(text)

print(headers[0][0].text)

for element in data:
    text = element.text
    #print(text)

driver.quit()
