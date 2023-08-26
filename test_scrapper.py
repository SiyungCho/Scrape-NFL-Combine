from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

from scrape_headers import col_names

path = Service("C:\\Users\\siyun\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
"""
NFL_url = 'https://nflcombineresults.com/nflcombinedata.php?year={yrs}&pos=&college='.format(yrs=2019)
driver = webdriver.Chrome(service=path)
driver.get(NFL_url)

data_table = []
table = driver.find_element(By.ID, 'datatable')
rows = table.find_elements(By.TAG_NAME, 'tr')

for row in rows[1:]:  # Skip the header row
    cols = row.find_elements(By.TAG_NAME, 'td')
    player_data = [col.text if col.text.strip() != '' else '0' for col in cols]
    data_table.append(player_data)

df = pd.DataFrame(data_table, columns=col_names)
print(df)

driver.quit()
"""
#data = driver.find_elements(By.TAG_NAME, "tbody")
#for element in data:
#    text = element.text
#all_values.append(text.split("\n"))
#driver.quit()

#for x in range(0, 10):
#    for y in range(0, 4):
#        print(all_values[x][y])
#print(all_values)

all_pro_players = []
for year in range(1987, 1989):

    NFL_url ='https://www.pro-football-reference.com/years/{yrs}/probowl.htm'.format(yrs=year)
    driver = webdriver.Chrome(service=path)
    driver.get(NFL_url)

    table = driver.find_element(By.ID, 'pro_bowl')
    rows = table.find_elements(By.TAG_NAME, 'tr')

    for row in rows[1:]:  # Skip the header row
        cols = row.find_elements(By.TAG_NAME, 'td')
        player_data = [col.text if col.text.strip() != '' else '0' for col in cols]
        all_pro_players.append(player_data)
    driver.quit()
print(all_pro_players)
"""
data_table = []
for year in range(1987, 2024):
    
    NFL_url = 'https://nflcombineresults.com/nflcombinedata.php?year={yrs}&pos=&college='.format(yrs=year)
    driver = webdriver.Chrome(service=path)
    driver.get(NFL_url)

    table = driver.find_element(By.ID, 'datatable')
    rows = table.find_elements(By.TAG_NAME, 'tr')

    for row in rows[1:]:  # Skip the header row
        cols = row.find_elements(By.TAG_NAME, 'td')
        player_data = [col.text if col.text.strip() != '' else '0' for col in cols]
        data_table.append(player_data)
    driver.quit()
"""   

all_pro_players = []
for year in range(1987, 2023):

    NFL_url ='https://www.pro-football-reference.com/years/{yrs}/probowl.htm'.format(yrs=year)
    driver = webdriver.Chrome(service=path)
    driver.get(NFL_url)

    data = driver.find_elements(By.TAG_NAME, "tbody")
    for element in data:
        text = element.text
    all_pro_players.append(text.split("\n"))
    driver.quit()