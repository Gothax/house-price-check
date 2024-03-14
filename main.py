import streamlit as st
import home
import page1
# from page2 import page2
# from page3 import page3
# from page4 import page4

def main():
    pages = {
        '홈': home,
        '페이지 1': page1,
        # '페이지 2': page2,
        # '페이지 3': page3,
        # '페이지 4': page4
    }

    st.sidebar.title('메뉴')
    selection = st.sidebar.radio('페이지 선택', list(pages.keys()))

    # 선택한 페이지 실행
    pages[selection]()

if __name__ == '__main__':
    main()
