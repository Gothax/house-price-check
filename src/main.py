import streamlit as st
from home import home
from transaction_price_map import price_map
from compare_price import compare_price
from age_gender import age_gender
from predict_price import predict_price
from business_district import business_district

def main():
    pages = {
        'Home': home,
        '아파트 실거래가(지도)': price_map,
        '월별 가격 비교': compare_price,
        '상권 분석': business_district,
        '동네별 연령대, 성별 분포': age_gender,
        '집값예측(Beta)': predict_price
    }

    st.sidebar.title('메뉴')
    selection = st.sidebar.radio(' ', list(pages.keys()))

    # 선택한 페이지 실행
    pages[selection]()



if __name__ == '__main__':
    main()
