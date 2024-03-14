import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from tqdm import tqdm
"""
실거래가를 지도에 표시해 주는 페이지
main.py에서 페이지 노출 시 price_map 호출 -> read_csv -> create_map -> 출력
"""

def read_csv_file(file_path):
    # CSV 파일을 읽어와 데이터프레임으로 변환하는 함수
    df = pd.read_csv(file_path, encoding='cp949')
    return df


def create_map(df):
    # 지도 생성
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=13)

    total = len(df)
    # 데이터프레임을 순회하며 마커 추가
    with tqdm(total=total, desc="진행 상태") as pbar:
        for index, row in df.iterrows():

            location = row[[''], ['']]
            popup = f"장소: {row['단지명']}\n가격: {row['거래금액(만원)']}"
            folium.Marker(location, popup=popup).add_to(m)
            pbar.update(1)  # 진행 상태 업데이트

    return m


def price_map():
    st.title('아파트 실거래가')
    st.write('Page1.')
    csv_file_path = 'data/아파트(매매)_실거래가_20240314104119.csv'
    df = read_csv_file(csv_file_path)
    
    # 지도 생성
    map = create_map(df)
    # 지도 출력
    folium_static(map)
