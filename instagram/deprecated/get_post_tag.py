#-*- coding: utf-8 -*-
## parser.py
import requests
from bs4 import BeautifulSoup
import json
import os

import sys





## python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

input_tag=input('입력하실 태그? ')

req=requests.get('https://www.instagram.com/sikugeon/')


html = req.text
soup = BeautifulSoup(html, 'html.parser')
scripts = soup.find_all('script')

data=""



for script in scripts:
    if 'window._sharedData = ' in script.text:
        data=str(script.text.strip())
        index=data.index('=')
        data=data[index+1:len(data)-1].strip() 

type(data)


test= json.loads(data)
post_number=0
s1=test['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][post_number]['node']['edge_media_to_caption']['edges'][0]['node']['text']
print(s1[s1.find("일상"):])


##print(test['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges'][0]['node']['display_url'])
with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as f:
    f.write(data)
    


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
