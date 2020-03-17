#-*- coding: utf-8 -*-
from selenium import webdriver

import bs4
import time



path = "Webdriver 경로를 입력합니다."
driver = webdriver.Chrome(r'C:\Users\myhome\Desktop\selenium\chromedriver.exe')
driver.get("http://google.com/")
search_box = driver.find_element_by_name("q")
search_box.send_keys("개발새발 블로그")
search_box.submit()
