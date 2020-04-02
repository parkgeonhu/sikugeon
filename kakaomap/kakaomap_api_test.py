import requests
import json
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from credential import config

query=input('입력하실 태그? ')
url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+query
headers = {'Authorization':'KakaoAK '+config.KAKAO_CONFIG['token']}

print(headers)

response=requests.get(url, headers=headers)
result=json.loads(response.text)


print(result["documents"][0]["address_name"])
print(result["documents"][0]['x'])
