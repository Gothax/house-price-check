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

# 주소 목록 파일 (.csv)
# data = pd.read_csv('data/test.csv', encoding='cp949')
data = pd.read_csv('data/아파트(매매)_실거래가_20240314104119.csv', encoding='cp949')


data['시군구'] = data['시군구'].astype(str)  # 시군구 열을 문자열로 변환
data['번지'] = data['번지'].astype(str)  # 번지 열을 문자열로 변환
data['주소'] = data['시군구'] + ' ' + data['번지']

# 네이버 지도 API 이용해서 위경도 찾기
geo_coordi = []     
for add in data['주소']:
    add_urlenc = parse.quote(add)  
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
        rescode = response.getcode()
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

    geo_coordi.append([latitude, longitude])


np_geo_coordi = np.array(geo_coordi)
pd_geo_coordi = pd.DataFrame({"도로명": data['주소'].values,
                              "위도": np_geo_coordi[:, 0],
                              "경도": np_geo_coordi[:, 1]})

pd_geo_coordi.to_csv('data/output.csv', encoding='utf-8-sig')