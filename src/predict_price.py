import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go


@st.cache_resource
def load_data():
    df = pd.read_excel("data/merged_file_with_predictions_latestver.xlsx")
    return df

def predict_price():
    st.title('집값 예측 (Beta)')

    df = load_data()

    # 사이드바 설정
    st.sidebar.header('동을 선택하고 아파트를 선택할 수 있어요!')

    # 법정동명 선택
    selected_dong = st.sidebar.selectbox('법정동명 선택', df['법정동명'].unique())

    # 선택된 법정동에 해당하는 도로명주소 선택
    selected_road_name = st.sidebar.selectbox('상세주소 선택',
                                            df[df['법정동명'] == selected_dong]['도로명'].unique())

    # 선택된 도로명주소에 해당하는 데이터 필터링
    filtered_df = df[df['도로명'] == selected_road_name]

    if not filtered_df.empty:
        # 단지명을 표시하기 위해 첫 번째 행의 데이터 사용
        complex_name = filtered_df.iloc[0]['단지명']
        st.write(f"{complex_name}아파트의 가격 예측")

        
    fig = go.Figure()
    offset = 0.15  # 막대 사이의 간격을 조절하기 위한 오프셋

    for i in range(len(filtered_df)):
        current_price = filtered_df.iloc[i]['price']
        predicted_price = filtered_df.iloc[i]['예측집값']
        percent_change = ((predicted_price - current_price) / current_price) * 100
        color = 'RoyalBlue' if predicted_price < current_price else 'Crimson'
        
         # 가격 단위 변환 (만원 -> 억원)
        current_price_fmt = f"{current_price // 10000}억 {current_price % 10000}만원" if current_price % 10000 != 0 else f"{current_price // 10000}억원"
        predicted_price_fmt = f"{predicted_price // 10000}억 {predicted_price % 10000}만원" if predicted_price % 10000 != 0 else f"{predicted_price // 10000}억원"

        # 호버 텍스트에 변동률 포함
        # hovertext = f"현재 가격: {current_price}<br>예측 가격: {predicted_price}<br>변동률: {'상승' if percent_change > 0 else '하락'} {abs(percent_change):.2f}%"
        hovertext = f"현재 가격: {current_price_fmt}<br>예측 가격: {predicted_price_fmt}<br>변동률: {'상승' if percent_change > 0 else '하락'} {abs(percent_change):.2f}%"

        fig.add_trace(go.Bar(x=[i - offset], y=[current_price], name='현재 가격', marker_color='LightSkyBlue', hovertemplate=hovertext, width=0.3))
        fig.add_trace(go.Bar(x=[i + offset], y=[predicted_price], name='예측 가격', marker_color=color, hovertemplate=hovertext, width=0.3))


    fig.update_layout(barmode='group', xaxis_tickangle=-45)

    st.plotly_chart(fig, use_container_width=True)