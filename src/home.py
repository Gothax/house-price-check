import streamlit as st
from transaction_price_map import price_map
from compare_price import compare_price

def home():
    st.title('HOME')
    st.subheader('WELCOME HOME! 이제 home을 구해보세요!')
    
    st.write(" ")

    st.markdown('**지도에서 보는 아파트 실거래가**')
    st.write("2023-04-14 ~ 2024-03-14에 매매된 아파트의 가격을 지도에서 볼 수 있습니다!")
    st.write("지도로 가고 싶은 지역, 동네를 골라보세요")
    st.write("1년간 매매된 실거래가 32,000개를 모두 볼 수 있어요")
    st.write("주변 상권도 제가 분석해 드릴게요!")
    st.write("마음에 드는 동네를 고르셨으면 가격 변동을 봐야겠죠? 월별 가격 비교 페이지를 사용해 보세요")
    
    st.image('data/1.png', caption='이미지 캡션', width=500)
    

    st.write('**월별 가격 비교**')
    st.write('2020년~현재까지 5년간의 실거래가를 모두 볼 수 있어요')
    st.write('원하는 동네의 평균 집값이 어떻게 변하고 있나 확인해 보세요!')
    st.image('data/2.png', caption='이미지 캡션', width=500)


    st.write('**동네별 연령대, 성별**')
    st.write('가격, 위치를 봤으니 동네 주민이 어떤 사람인가 확인해 보세요!')
    st.write('')


    st.write('**집값 예측 (Beta)**')
    st.write('위의 모든 지표 그리고 저만의 지표를 이용해 언제 집을 사는게 좋을지, 나중에 집값이 어떻게 변할 지 예측해 드릴게요!')



    st.write("동네별 주요 연령대, 성별분포도 볼 수 있어요")