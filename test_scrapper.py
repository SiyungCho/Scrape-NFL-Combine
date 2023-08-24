from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:\\Users\\siyun\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
all_values = list()
for year in range(2022, 2024):
    
    NFL_url = 'https://nflcombineresults.com/nflcombinedata.php?year={yrs}&pos=&college='.format(yrs=year)
    driver = webdriver.Chrome(service=path)
    driver.get(NFL_url)

    data = driver.find_elements(By.TAG_NAME, "tbody")
    for element in data:
        text = element.text
    all_values.append(text.split("\n"))
    driver.quit()
for x in range(0, 10):
    for y in range(0, 4):
        print(all_values[x][y])
print(all_values)
    