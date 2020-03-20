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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from credential import config
from multiprocessing import Pool, Process, Queue


SCROLL_PAUSE=1

TARGET_ID='sikugeon'


def get_driver():

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    # UserAgent값을 바꿔줍시다!
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    options.add_argument("lang=ko_KR")
   
    driver = webdriver.Chrome('../util/chromedriver.exe', options=options)

    driver.get('about:blank')
    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
 
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
##    later_btn = driver.find_element_by_class_name("HoLwm")
##
##    later_btn.click()

    return driver


def get_follower_list():
    driver=get_driver()
    print(2)
    driver.get("https://www.instagram.com/"+TARGET_ID)
    time.sleep(2)


    follower_count= WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) a > span'))
    ).get_attribute("title").replace(",","")

    
    driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2)').click()

    time.sleep(2)
    
    dialog = driver.find_element_by_class_name("isgrP")

    last_height = driver.execute_script("return arguments[0].scrollHeight;", dialog)

    while True:
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", dialog)
        time.sleep(SCROLL_PAUSE)

        new_height = driver.execute_script("return arguments[0].scrollHeight;", dialog)
        if new_height == last_height:
            break
        last_height = new_height

    #렌더링 대기
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    followers = soup.find_all('a', class_= '_0imsa')

    follower_list=[]

    for follower in followers:
        print(follower.text)
        follower_list.append(follower.text)


    time.sleep(1)
    

    return follower_list



def get_following_list():
    driver=get_driver()
    driver.get("https://www.instagram.com/"+TARGET_ID)
    
    time.sleep(2)

    follower_count= WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) a > span'))
    ).get_attribute("title").replace(",","")
    
    driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3)').click()

    time.sleep(2)


    dialog = driver.find_element_by_class_name("isgrP")

    last_height = driver.execute_script("return arguments[0].scrollHeight;", dialog)

    while True:
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", dialog)
        time.sleep(SCROLL_PAUSE)

        new_height = driver.execute_script("return arguments[0].scrollHeight;", dialog)
        if new_height == last_height:
            break
        last_height = new_height

    #렌더링 대기
    time.sleep(1)
    
    soup = BeautifulSoup(driver.page_source, 'lxml')

    followings = soup.find_all('a', class_= '_0imsa')

    following_list=[]

    for following in followings:
        print(following.text)
        following_list.append(following.text)


    time.sleep(1)
    
    return following_list




def export_data(data, name):
    with open(os.path.join(BASE_DIR, name), 'w+') as f:
        for item in data:
            f.write(item+' ')
    
    


if __name__ == "__main__":

    followings=get_following_list()
    followers=get_follower_list()

    print(len(followings))
    print(len(followers))


    followers_set=set(followers)
    followings_set=set(followings)
    
    export_data(list(followings_set-followers_set), '1.txt')
    export_data(list(followers_set-followings_set), '2.txt')
    
    
##    export_data(followers_set-followings_set, '1.txt')
##    export_data(followings_set-followers_set, '2.txt')



    
