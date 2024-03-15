import streamlit as st
import pandas as pd
import folium
from folium import plugins
from streamlit_folium import folium_static
"""
실거래가를 지도에 표시해 주는 페이지
main.py에서 페이지 노출 시 price_map 호출 -> read_csv -> create_map -> 출력
"""

@st.cache_resource
def read_csv_file(file_path):
    # # CSV 파일을 읽어와 데이터프레임으로 변환하는 함수
    # df = pd.read_csv(file_path, encoding='cp949')

     # XLSX 파일을 읽어와 데이터프레임으로 변환하는 함수
    df = pd.read_excel(file_path)
    return df


@st.cache_resource
def create_map(df):
    # 지도 생성
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=13)
    m_c = plugins.MarkerCluster()

    # 데이터프레임을 순회하며 마커 추가
    for row in df.itertuples():
        location = [row.위도, row.경도]

        if pd.isna(location[0]) or pd.isna(location[1]):  # NaN 값을 처리
            continue

        popup = f"장소: {row.단지명}\n가격: {row.price.lstrip()}"
        m_c.add_child(folium.Marker(location, popup=popup))

    m.add_child(m_c)
    return m


@st.cache_resource
def price_map():
    st.title('지도로 보는 아파트 실거래가')
    st.write('최근 1년간 발생한 거래의 가격을 볼 수 있습니다.')
    st.write('계약일자 : 2023-04-14 ~ 2024-03-14')
    csv_file_path = 'data/output_usethis_2304_2403.xlsx'
    df = read_csv_file(csv_file_path)

    m = create_map(df)
    folium_static(m, width=800, height=600)
