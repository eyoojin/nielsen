from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import csv

local_file_path = '/home/ubuntu/damf2/nielsen/data/tv3/'

def save_to_csv(data, date): 
    file_date = f"{date}.csv"
    with open(local_file_path + file_date, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

driver = webdriver.Chrome()

URL = 'https://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=3_1&area=01&begin_date=202502'
driver.get(URL)

year = driver.find_element(By.CSS_SELECTOR, '#select > option[value="2025"]')
year.click()
time.sleep(1)


month = driver.find_element(By.CSS_SELECTOR, '#select2 > option[value="03"]')
month.click()
# time.sleep(1)

for i in range(1, 32):
    if i < 10:
        day = driver.find_element(By.CSS_SELECTOR, f'#select1 > option[value="0{i}"]')
        day.click()    
    else:
        day = driver.find_element(By.CSS_SELECTOR, f'#select1 > option[value="{i}"]')
        day.click()
# time.sleep(1)

    search_button = driver.find_element(By.CSS_SELECTOR, 'img[onclick="goSearch();"]')
    search_button.click()
# time.sleep(1)

    td_list = driver.find_elements(By.CSS_SELECTOR, 'td')
    td_texts = [td.text for td in td_list]

    result = []
    for text in td_texts:
        result.append(text)

    # print(result)
# print(result[12])
    print(result[13])
# print(result[14])
    rlist = result[14].split('\n')

    answer = []
    exceptions = [
    "TV CHOSUN", "SBS Plus", "KBS Drama", "KBS JOY", "MBC every1",
    "MBC SPORTS+", "SBS Sports", "KBS N 스포츠", "EBS 플러스", "EBS English",
    "EBS 키즈", "National Geographic", "Discovery Channel", "Channel CGV",
    "JEI 재능TV", "대교 어린이TV", "tvN STORY", "SPOTV Prime"
]

    for r in rlist:
        for ex in exceptions:
            r = r.replace(ex, ex.replace(" ", ""))
        r = r.split(' ')
        answer.append(r)
    print(answer[3:])

# columns = ['순위', '채널', '프로그램', '시청률']

# df = pd.DataFrame(data=answer[3:], columns=columns)

# df.to_csv('/home/ubuntu/damf2/data/nielsen/2024-07-01.csv', sep=',')

    save_to_csv(answer[3:], result[13])