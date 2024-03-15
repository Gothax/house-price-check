import pandas as pd

# 엑셀 파일 읽기
df = pd.read_excel('data/지역별나이_성별.xlsx')

# # 필요한 열 선택
# df = df.iloc[:, 4:114]  # 0세 남자부터 110세 남자까지의 열 선택

# # 연령대 구분을 위한 리스트 생성
# age_groups = [f'{i}대 남자' for i in range(0, 110, 10)]

# # 연령대별로 합계 계산
# df_sum = pd.DataFrame(df.sum(), columns=['합계'])
# df_sum.index = age_groups

# # 새로운 엑셀 파일 생성
# df_sum.to_excel('새로운_파일.xlsx')


for comp in df:
    print(comp)