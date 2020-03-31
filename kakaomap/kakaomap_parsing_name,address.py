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
 
    driver.get("http://kko.to/ryCuEQw0o")
    time.sleep(5)


    return driver

def get_sikugeon_list():
    driver=get_driver()
    dialog= WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#other\.favorite > ul'))
        )

    print(dialog.get_attribute('innerHTML'))
    soup = BeautifulSoup(dialog.get_attribute('innerHTML'), 'lxml')

    entire = soup.find_all('a', class_= 'link_txt')

    test = soup.find_all('div', class_= 'FavoriteInformationBundle')

    for entity in test:
        temp = BeautifulSoup(str(entity), 'lxml')
        address= temp.find('span', class_= 'desc_region')
        name=temp.find('a', class_= 'link_txt')
        print(str(name.text)+" "+str(address.text))
   
##    stores_address =soup.find_all('span', class_= 'link_txt')

    places=[]

    for place in entire:
        print(place.text)
        places.append(place.text)
    print(len(places))






def export_data(data, name):
    with open(os.path.join(BASE_DIR, name), 'w+') as f:
        for item in data:
            f.write(item+' ')
    
    


if __name__ == "__main__":
    get_sikugeon_list()



##    export_data(followers_set-followings_set, '1.txt')
##    export_data(followings_set-followers_set, '2.txt')



    
