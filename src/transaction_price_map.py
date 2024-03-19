import streamlit as st
import pandas as pd
import folium
from folium import plugins
from streamlit_folium import folium_static
from folium import Popup
"""
실거래가를 지도에 표시해 주는 페이지
main.py에서 페이지 노출 시 price_map 호출 -> read_csv -> create_map -> 출력
"""

@st.cache_resource
def read_csv_file(file_path):
     # XLSX 파일을 읽어와 데이터프레임으로 변환하는 함수
    df = pd.read_excel(file_path)
    return df

# 3만개의 데이터를 marker cluster로 표시
# 단지명, 가격, 예측가격 표시
def create_map(df):
    # 지도 생성
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=13)
    m_c = plugins.MarkerCluster()

    # 데이터프레임을 순회하며 마커 추가
    for row in df.itertuples():
        location = [row.위도, row.경도]

        # NaN 값을 처리
        if pd.isna(location[0]) or pd.isna(location[1]):  
            continue

        popup_html = f"<b>단지명:</b> {row.단지명}<br><b>가격:</b> {row.price}<br><b>평수:</b>{row.평수}(㎡)<br><b>예측집값:</b> {row.예측집값}"
        popup = Popup(popup_html, max_width=300)
        styled_popup = folium.Popup(folium.Html(f'<div style="font-size: 12pt; font-family: Arial;">{popup_html}</div>', script=True), max_width=300)

        m_c.add_child(folium.Marker(location, popup=styled_popup))

    m.add_child(m_c)
    return m


def price_map():
    st.title('지도로 보는 아파트 실거래가')
    st.write('최근 1년간 발생한 거래의 가격을 볼 수 있습니다.')
    st.write('계약일자 : 2023-04-14 ~ 2024-03-14')
    st.write('어살이 제공한 예측 집값은 참고로 사용해 주세요!')
    csv_file_path = 'data/merged_file_with_predictions_latestver.xlsx'
    df = read_csv_file(csv_file_path)

    m = create_map(df)
    folium_static(m, width=800, height=600)
