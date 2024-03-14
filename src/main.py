import streamlit as st
from home import home
from transaction_price_map import price_map

def main():
    pages = {
        'Home': home,
        '아파트 실거래가': price_map,
        # '페이지 2': page2,
        # '페이지 3': page3,
        # '페이지 4': page4
    }

    st.sidebar.title('메뉴')
    selection = st.sidebar.radio(' ', list(pages.keys()))

    # 선택한 페이지 실행
    pages[selection]()



if __name__ == '__main__':
    main()
