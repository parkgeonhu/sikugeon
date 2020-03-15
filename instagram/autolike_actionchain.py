#-*- coding: utf-8 -*-
## parser.py
from selenium import webdriver

from bs4 import BeautifulSoup
import time

from selenium.webdriver.common.keys import Keys

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from credential import config




path = "Webdriver 경로를 입력합니다."
driver = webdriver.Chrome('../util/chromedriver.exe')
driver.get("https://www.instagram.com/")


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


entire = driver.find_element_by_class_name("cGcGK")

source=driver.page_source

soup = BeautifulSoup(source, 'lxml')

print(entire.get_attribute('innerHTML'))

time.sleep(5)

for i in range(10):
    time.sleep(1.5)
    like_btns=driver.find_elements_by_class_name("fr66n")
    like_btns[i].click()
    print(like_btns)

print("mmmmmmmmmmmmmmmmmmm")

##print(like_btn.get_attribute('innerHTML'))



##for like_btn in like_btns:
##    like_btn.click()
##    print(like_btn.get_attribute('innerHTML'))
####    like_btn.clear()
####    print()
##    print('----------------------------------------')
####    driver.execute_script("arguments[0].click();", like_btn)
####    time.sleep(2)
##
##
####like_btn.click()














##
##
##
#### python파일의 위치
##BASE_DIR = os.path.dirname(os.path.abspath(__file__))
##
##input_tag=input('입력하실 태그? ')
##
##req=requests.get('https://www.instagram.com/explore/tags/'+input_tag)
##
##
##html = req.text
##soup = BeautifulSoup(html, 'html.parser')
##scripts = soup.find_all('script')
##
##data=""
##
##
##
##for script in scripts:
##    if 'window._sharedData = ' in script.text:
##        data=str(script.text.strip())
##        index=data.index('=')
##        data=data[index+1:len(data)-1].strip() 
##
##type(data)
##
##test= json.loads(data)
##print(test['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['count'])
##
##with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as f:
##    f.write(data)
    


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
