import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
#주소를 위도 경도 값으로 바꿔주기 위해 import
from geopy.geocoders import Nominatim
geo_local = Nominatim(user_agent='South Korea')


def read_csv_file(file_path):
    # CSV 파일을 읽어와 데이터프레임으로 변환하는 함수
    df = pd.read_csv(file_path, encoding='cp949')
    return df


def create_map(df):
    # 지도 생성
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=13)

    # 데이터프레임을 순회하며 마커 추가
    for index, row in df.iterrows():
        add = row['시군구'] + row['번지']
        location = geocoding(add)
        popup = f"장소: {row['단지명']}\n가격: {row['거래금액(만원)']}"
        folium.Marker(location, popup=popup).add_to(m)

    return m


# 위도, 경도 반환하는 함수
def geocoding(address):
    try:
        geo = geo_local.geocode(address)
        x_y = [geo.latitude, geo.longitude]
        return x_y

    except:
        return [0,0]


def price_map():
    st.title('아파트 실거래가')
    st.write('Page1.')
    # CSV 파일 경로
    csv_file_path = 'data/아파트(매매)_실거래가_20240314104119.csv'
    # CSV 파일 읽어오기
    df = read_csv_file(csv_file_path)
    # 지도 생성
    map = create_map(df)
    # 지도 출력
    folium_static(map)
