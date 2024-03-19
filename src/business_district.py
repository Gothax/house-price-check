import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static
import json
from folium import plugins
import random
"""
상권분석 페이지
main에서 business distric호출 -> load data -> create map

"""



# 데이터 로딩 함수
@st.cache_resource
def load_data(geojson_path, excel_path):
    with open(geojson_path, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)
    df = pd.read_excel(excel_path)
    return geojson_data, df

# 지도 생성 함수
# 행정동구역 경계값 geojson을 활용해서 경계를 표시
# 구역당 마커 하나가 아닌 이유
# 상권데이터의 주소 기준은 법정동, 경계값은 행정동 -> 전처리 실패
# 대체하기 위해 실 거래가에 있는 경도, 위도를 활용해 중복을 제거후 마커 추가
def create_map(df, seoul_geojson):
    # 중복 위치 제거
    df['위치'] = df[['위도', '경도']].apply(tuple, axis=1)  # 위도와 경도를 튜플로 묶어 새로운 컬럼 생성
    unique_locations = df['위치'].unique()  # 유니크한 위치 정보만 추출

    m = folium.Map(location=[37.57, 126.97], zoom_start=11)

    # 경계구역 데이터를 지도에 추가
    folium.GeoJson(
        seoul_geojson,
        name='seoul',
        style_function=lambda feature: {
            'fillColor': "#{:06x}".format(random.randint(0, 0xFFFFFF)), # 무작위 색상
            'color': 'black',
            'weight': 2,
            'dashArray': '5, 5'
        }
    ).add_to(m)

    marker_cluster = plugins.MarkerCluster().add_to(m)

    for location in unique_locations:
        subset = df[df['위치'] == location]  # 동일한 위치에 있는 데이터만 필터링

        popup_text = "<div style='width:200px;'><ul style='margin:0; padding:0;'>"

        popup_text += "".join([f"<li style='list-style-type:none;'><b>{k}:</b> {v}</li>" for k, v in subset.iloc[0][['과학·기술', '교육', '보건의료', '부동산', '소매', '수리·개인', '숙박', '시설관리·임대', '예술·스포츠', '음식']].items()])
        
        popup_text += "</ul></div>"

        popup = folium.Popup(popup_text, max_width=2650)

        folium.Marker(
            location=location,
            icon=folium.Icon(color='green', icon='star'),
            popup=popup_text,
        ).add_to(marker_cluster)

    return m

def business_district():
    st.title('상권 분석')

    geojson_path = 'data/hangjeongdong_서울특별시.geojson'
    excel_path = 'data/merged_file_with_predictions_latestver.xlsx'
    
    # 데이터 로딩
    seoul_geojson, df = load_data(geojson_path, excel_path)

    # 지도 생성 및 표시
    m = create_map(df, seoul_geojson)
    folium_static(m)

