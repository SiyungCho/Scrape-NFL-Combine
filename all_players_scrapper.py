from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:\\Users\\siyun\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
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
