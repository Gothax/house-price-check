import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

@st.cache_resource
def read_excel_file(file_path):
    df = pd.read_excel(file_path)
    return df

def preprocess_data(df, selected_year):
    df['월'] = df['계약년월'] - (int(selected_year)*100)
    return df

def plot_price_by_month(df, selected_gu):
    # 선택한 '구'에 해당하는 데이터 필터링
    filtered_df = df[df['시군구'] == selected_gu]
    # 월별 가격 평균 계산
    monthly_avg_price = filtered_df.groupby('월')['price'].mean()
    
    # 시각화
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=monthly_avg_price.index, y=monthly_avg_price.values, ax=ax)
    ax.set_xlabel('month')
    ax.set_ylabel('average price')
    # ax.set_title(f'average price of {year}')

    # x축 눈금 설정
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_major_formatter(ticker.ScalarFormatter())

    # x축 눈금 레이블 설정
    ax.set_xticklabels([f'{int(tick)}' for tick in ax.get_xticks()])

    st.pyplot(fig)

def compare_price():
    st.title('월별 가격 비교')
    
    # 년도 선택 사이드바
    selected_year = st.sidebar.selectbox('년도 선택', ['2024', '2023', '2022', '2021', '2020'])

    excel_file_path = f'data/{selected_year}.xlsx'
    df = read_excel_file(excel_file_path)
    
    if df['price'].dtype == str:  # 'price' 열이 int 형식인 경우에만 실행
        df['price'] = df['price'].str.replace(',', '')  # 쉼표(,) 제거
        df['price'] = df['price'].astype(int)
    
    df = preprocess_data(df, selected_year)

    # 서울시 자치구 리스트
    seoul_gu_list = df['시군구'].unique()

    # '구' 선택 사이드바
    selected_gu = st.sidebar.selectbox('동 선택', seoul_gu_list)


    st.write(f'{selected_gu}의 {selected_year}년 월별 평균 가격')
    st.write('단위는 만원입니다.')
    st.write(f'해당 년도에 거래가 없었다면 데이터가 나오지 않습니다,')

    
    # 선택한 '구'에 따른 가격 그래프 출력
    plot_price_by_month(df, selected_gu)




