#-*- coding: utf-8 -*-
## parser.py
from selenium import webdriver

from bs4 import BeautifulSoup
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from credential import config

def get_driver():
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

    return driver

def followLiker(id_list):
    driver=get_driver()
    id_list=['sanha_1.17']

    for id in id_list:
        driver.get("https://www.instagram.com/"+id)
        time.sleep(2)

        follower_count= WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) a > span'))
            ).get_attribute("title").replace(",","")
        
        post_count= WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(1) > span > span'))
            ).text.replace(",","")


        print(follower_count)
        print(post_count)

        
        first_post_xpath = '//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]'
        first_post = driver.find_element_by_class_name("eLAPa").click()
        
        driver.implicitly_wait(5)
        
##        for i in range(16):
##            post_like_btn = driver.find_element_by_class_name("fr66n")
##            driver.find_element_by_class_name("fr66n").click()
##            time.sleep(1)
##            ##수정 봐야 할 로직 range variable이 
##            driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
##            time.sleep(1)




##
##    print(follower_count)
##

##    driver.find_element_by_class_name("vBF20").click()


    

if __name__ == "__main__":
    followLiker([])

