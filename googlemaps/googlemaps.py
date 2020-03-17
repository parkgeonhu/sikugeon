#-*- coding: utf-8 -*-
from selenium import webdriver

from bs4 import BeautifulSoup
import time



path = "Webdriver 경로를 입력합니다."
driver = webdriver.Chrome(r'C:\Users\myhome\Desktop\selenium\chromedriver.exe')
driver.get("https://www.google.com/maps/@/data=!3m1!4b1!4m3!11m2!2scjKYe9Nzb5duDEo4Xrctbk0KuBJyOw!3e3?shorturl=1")
##search_box = driver.find_element_by_name("q")


time.sleep(5)

source=driver.page_source

soup = BeautifulSoup(source, 'lxml')

entire = soup.find('div', class_='section-layout section-scrollbox scrollable-y scrollable-show')

##section_result_content=soup.find_all('h3', class_='section-result-title')

titles = entire.find_all('span')

sikugeon_list=[]

for title in titles:
    sikugeon_list.append(title.text)

print(sikugeon_list)
