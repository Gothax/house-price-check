import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
"""
행정동구역을 기준으로 거주중인 인구수를 성별, 연령대로 구분
그래프로 시각화
main -> age gender 호출
처리할 데이터가 많지 않아 캐시 처리 X
"""

def age_gender():
    # 마이너스 기호가 정상적으로 표시되도록 설정

    st.title('동네별 성비 및 연령대 분포 시각화')

    df = pd.read_excel('data/compressed_data_complete.xlsx')

    selected_dong = st.sidebar.selectbox('동네 선택', df['읍면동명'].astype(str).unique())

    # 선택된 동네에 해당하는 데이터를 필터링
    filtered_data = df[df['읍면동명'] == selected_dong]

    # 성별 및 연령대별 분포를 시각화
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))

    # 남자 인구 분포
    # '0~9세남자'부터 '110세 이상남자'까지의 열 선택을 위한 수정
    ax[0].bar(filtered_data.columns[5:17], filtered_data.iloc[0, 5:17], color='blue', label='male')
    ax[0].set_title(f'{selected_dong} - male')
    ax[0].set_ylabel('population')
    ax[0].legend()

    # '0~9세여자'부터 '110세 이상여자'까지의 열 선택을 위한 수정
    ax[1].bar(filtered_data.columns[18:], filtered_data.iloc[0, 18:], color='red', label='female')
    ax[1].set_title(f'{selected_dong} - female')
    ax[1].set_ylabel('population')
    ax[1].legend()

    st.pyplot(fig)

    