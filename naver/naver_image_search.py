import requests
import json
from bs4 import BeautifulSoup as bs

query=input('입력하실 태그? ')
url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='+'합정동오레노라멘'

response=requests.get(url)


soup = bs(response.text, "lxml")
imgs = soup.find(class_='_img')

n=1
imgUrl = imgs['data-source']

print(imgUrl)

##
##for i in imgs:
##    imgUrl = i['data-source']
##    print(imgUrl)
####    with requests.get(imgUrl) as f:
####        with open('./img/' + query + str(n)+'.jpg','wb') as h: # w - write b - binary
####            img = f.read()
####            h.write(img)
##    n += 1
