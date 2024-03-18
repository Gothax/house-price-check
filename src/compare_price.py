import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

@st.cache_resource
def read_excel_file(file_path):
    df = pd.read_excel(file_path)
    return df

def preprocess_data(df):
    # 계약년월에서 년도를 빼고 월만 남김
    df['월'] = df['계약년월'] % 100
    return df

def plot_price_by_month(df, selected_gu):
    filtered_df = df[df['시군구'] == selected_gu]
    monthly_avg_price = filtered_df.groupby('월')['price'].mean()  # 여기서 'price'가 숫자 타입인지 확인 필요
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=monthly_avg_price.index, y=monthly_avg_price.values, ax=ax)
    ax.set_xlabel('Month')
    ax.set_ylabel('Average Price')
    
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
    ax.set_xticklabels([f'{int(tick)}' for tick in ax.get_xticks()])  # 월 표시 수정
    
    st.pyplot(fig)

def compare_price():
    st.title('월별 가격 비교')
    
    selected_year = st.sidebar.selectbox('년도 선택', ['2024', '2023', '2022', '2021', '2020'])
    excel_file_path = f'data/{selected_year}.xlsx'
    df = read_excel_file(excel_file_path)

    # 'price' 열이 숫자 타입이 아닐 경우 문자열로 변환 및 쉼표 제거 후 숫자 타입으로 변환
    if not pd.api.types.is_numeric_dtype(df['price']):
        df['price'] = df['price'].astype(str).str.replace(',', '').astype(int)
    
    df = preprocess_data(df)
    
    seoul_gu_list = df['시군구'].unique()
    selected_gu = st.sidebar.selectbox('구 선택', seoul_gu_list)
    
    st.write(f'{selected_gu}의 {selected_year}년 월별 평균 가격')
    st.write('단위는 만원입니다.')
    
    plot_price_by_month(df, selected_gu)
