#-*- coding: utf-8 -*-
## parser.py
from selenium import webdriver
import json
from bs4 import BeautifulSoup
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from credential import config




path = "Webdriver 경로를 입력합니다."
driver = webdriver.Chrome('../util/chromedriver.exe')
driver.get("http://www.instagram.com/")


time.sleep(1)


id=config.INSTAGRAM_CONFIG['id']
pw=config.INSTAGRAM_CONFIG['pw']


username = driver.find_element_by_name("username")
username.send_keys(id)
password = driver.find_element_by_name("password")
password.send_keys(pw)

login_btn = driver.find_element_by_class_name("L3NKy")


login_btn.click()

time.sleep(5)
later_btn = driver.find_element_by_class_name("HoLwm")

later_btn.click()

driver.get("https://www.instagram.com/sikugeon")

time.sleep(2)

follower_count= WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) a > span'))
    ).text.replace(",","")


#팔로워 클릭
driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2)').click()


print(follower_count)

dialog = driver.find_element_by_class_name("isgrP")

##for i in range(10):
##    driver.execute_script("arguments[0].scroll({top:10000});", dialog)
##    time.sleep(0.5)

time.sleep(2)



## python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


soup = BeautifulSoup(driver.page_source, 'lxml')

followers = soup.find_all('a', class_= '_0imsa')

follower_list=[]

for follower in followers:
    follower_list.append(follower.text)

print(follower_list)
print(len(follower_list))

##scripts = soup.find_all('script')

##for script in scripts:
##    if 'window._sharedData = ' in script.text:
##        data=str(script.text.strip())
##        index=data.index('=')
##        data=data[index+1:len(data)-1].strip() 
##
##test= json.loads(data)
##
with open(os.path.join(BASE_DIR, 'follower.json'), 'w+') as f:
    for item in follower_list:
        f.write(item+' ')
    
##my_titles = soup.select(
##    'h3 > a'
##    )

##data = {}
##
##for title in my_titles:
##    data[title.text] = title.get('href')
##
##with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
##    json.dump(data, json_file)
##
##print(data)
