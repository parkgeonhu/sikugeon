#-*- coding: utf-8 -*-
from selenium import webdriver

from bs4 import BeautifulSoup
import time

from selenium.webdriver.common.keys import Keys



path = "Webdriver 경로를 입력합니다."
driver = webdriver.Chrome(r'C:\Users\myhome\Desktop\selenium\chromedriver.exe')
driver.get("https://www.google.com/maps/@/data=!3m1!4b1!4m3!11m2!2scjKYe9Nzb5duDEo4Xrctbk0KuBJyOw!3e3?shorturl=1")
##search_box = driver.find_element_by_name("q")


time.sleep(5)

element = driver.find_element_by_class_name("section-scrollbox")

print(element.get_attribute('innerHTML'))

for count in range(10):
    driver.execute_script("arguments[0].scroll({top:10000});", element)
    time.sleep(1)



time.sleep(5)

source=driver.page_source

soup = BeautifulSoup(source, 'lxml')

section_result_titles=soup.find_all('h3', class_='section-result-title')

sikugeon_list=[]

for section_result_title in section_result_titles:
    title = section_result_title.find('span')
    sikugeon_list.append(title.text)
    


##titles = entire.find_all('span')
##
##sikugeon_list=[]
##
##for title in titles:
##    sikugeon_list.append(title.text)

print(sikugeon_list)
print(len(sikugeon_list))
