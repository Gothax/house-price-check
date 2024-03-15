import pandas as pd

data = pd.read_excel('data/output_usethis.xlsx')

# NaN 값이 있으면 찾아준다
print(data[data.isna( ).any(axis=1)])


import numpy as np
import pandas as pd
from urllib.request import urlopen
from urllib import parse
from urllib.request import Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
from dotenv import load_dotenv
import os
load_dotenv()
client_id = os.getenv("ClientID")
client_pw = os.getenv("ClientSecret")



api_url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='

# 주소 목록 파일 (.xlsx)
# data = pd.read_excel('data/xlver_test.xlsx', usecols='B, C, F, G, H, I, J', names=['시군구', '번지', '단지명', '전용면적(㎡)', '계약년월', '계약일', '거래금액(만원)'])

address_list = ['서울 구로구 항동로 72']

# 네이버 지도 API 이용해서 위경도 찾기
for add in address_list:
    add_urlenc = parse.quote(add)   # 주소를 URL에서 사용할 수 있도록 URL Encoding
    url = api_url + add_urlenc
    request = Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_pw)
    try:
        response = urlopen(request)
    except HTTPError as e:
        print('HTTP Error!')
        latitude = None
        longitude = None
    else:
        rescode = response.getcode()  # 정상이면 200 리턴
        if rescode == 200:
            response_body = response.read().decode('utf-8')
            response_body = json.loads(response_body)   # json
            if response_body['addresses'] == [] :
                print("'result' not exist!")
                latitude = None
                longitude = None
            else:
                latitude = response_body['addresses'][0]['y']
                longitude = response_body['addresses'][0]['x']
        else:
            print('Response error code : %d' % rescode)
            latitude = None
            longitude = None

    print(add, [latitude, longitude])





