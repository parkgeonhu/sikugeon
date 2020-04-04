#-*- coding: utf-8 -*-
## parser.py
import requests
from bs4 import BeautifulSoup
import json
import os

import sys

cover_url=[]
tags=[]

def get_next_page(query_hash, user_id, has_next_page, end_cursor):
    global cover_url
    global tags
    if has_next_page is False:
        return
    else:
        next_url = 'https://www.instagram.com/graphql/query/?query_hash='+query_hash+'&variables={"id":"'+user_id+'","first":12,"after":"'+end_cursor+'"}'
        req = requests.get(next_url)
        temp = json.loads(req.text)
        for entry in temp['data']['user']['edge_owner_to_timeline_media']['edges']:
            text=entry['node']['edge_media_to_caption']['edges'][0]['node']['text']
            tag=''
            idx=text.find('#식후건')
            if idx != -1:
                tag=text[idx:]
            tags.append(tag)
            cover_url.append(entry['node']['display_url'])
        _has_next_page = temp['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
##        if _has_next_page is 'true':
##            _has_next_page = True
##        else:
##            _has_next_page = False
        _end_cursor = temp['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
        get_next_page(query_hash, user_id, _has_next_page, _end_cursor )
        
        


## python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

##input_tag=input('입력하실 태그? ')

req=requests.get('https://www.instagram.com/sikugeon/?__a=1')


html = req.text
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


test= json.loads(html)
post_number=0

for entry in test['graphql']['user']['edge_owner_to_timeline_media']['edges']:
    cover_url.append(entry['node']['display_url'])

print(test['graphql']['user']['id'])

user_id=test['graphql']['user']['id']
end_cursor=test['graphql']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
has_next_page=test['graphql']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']

query_hash='d496eb541e5c789274548bf473cc553e'

next_url='https://www.instagram.com/graphql/query/?query_hash='+query_hash+'&variables={"id":"'+user_id+'","first":12,"after":"'+end_cursor+'"}'

get_next_page(query_hash, user_id, has_next_page, end_cursor)


print(len(cover_url))
print(len(tags))

##
##req=requests.get(next_url)
##print(req.text)


##s1=test['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][post_number]['node']['edge_media_to_caption']['edges'][0]['node']['text']
##print(s1[s1.find("일상"):])


##print(test['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges'][0]['node']['display_url'])
with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as f:
    f.write(str(cover_url))
    


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
