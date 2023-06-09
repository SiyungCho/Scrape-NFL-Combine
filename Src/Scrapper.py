#C:\Users\siyun\Downloads\WebScrappingBets\.venv\Scripts\python.exe
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pandas as pd

path = Service("C:\\Users\\siyun\\Downloads\\chromedriver_win32\\chromedriver.exe")
NFL_url = 'https://nflcombineresults.com/nflcombinedata.php?'

driver = webdriver.Chrome(service=path)
driver.get(NFL_url)

headers = driver.find_elements(By.TAG_NAME, "thead")
for element in headers:
    text = element.text

col_names = text.split("\n")
col_names = col_names[:-1] + col_names[-1].split(' ')
col_names.remove('Wonderlic')
print(col_names)

data = driver.find_elements(By.TAG_NAME, "tbody")
for element in data:
    text = element.text

all_values = text.split("\n")
print(all_values)

driver.quit()
