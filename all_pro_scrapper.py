from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:\\Users\\siyun\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
all_pro_players = []
for year in range(1987, 2023):

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