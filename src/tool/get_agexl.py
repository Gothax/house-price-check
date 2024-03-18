import pandas as pd

# 데이터를 읽어옵니다.
df = pd.read_excel('test_age_gender.xlsx')

# 나이대별로 분류합니다. 0~9세, 10~19세, ..., 100~109세, 110세 이상
age_ranges = [(0,9), (10,19)] + [(i, i+9) for i in range(20, 100, 10)] + [(100, 109), (110, 999)]
age_range_labels = ['0~9세', '10~19세'] + [f'{i}~{i+9}세' for i in range(20, 100, 10)] + ['100~109세', '110세 이상']

# 새로운 DataFrame을 생성합니다.
new_df = pd.DataFrame()

for start, end in age_ranges:
    # 남자
    if start == 110:  # '110세 이상'의 경우
        new_df['110세 이상남자'] = df['110세이상 남자']
    else:
        male_col = [f'{i}세남자' for i in range(start, min(end, 109)+1)]
        new_df[f'{start}~{end}세남자'] = df[male_col].sum(axis=1)
    
    # 여자
    if start == 110:  # '110세 이상'의 경우
        new_df['110세 이상여자'] = df['110세이상 여자']
    else:
        female_col = [f'{i}세여자' for i in range(start, min(end, 109)+1)]
        new_df[f'{start}~{end}세여자'] = df[female_col].sum(axis=1)

# 읍면동명과 기본 정보를 새로운 DataFrame에 추가합니다.
new_df['행정기관코드'] = df['행정기관코드']
new_df['기준연월'] = df['기준연월']
new_df['시도명'] = df['시도명']
new_df['시군구명'] = df['시군구명']
new_df['읍면동명'] = df['읍면동명']

# 새로운 순서를 정의합니다.
columns_order = ['행정기관코드', '기준연월', '시도명', '시군구명', '읍면동명'] + [f'{start}~{end}세남자' for start, end in age_ranges if start < 110] + ['110세 이상남자'] + [f'{start}~{end}세여자' for start, end in age_ranges if start < 110] + ['110세 이상여자']
new_df = new_df[columns_order]

# 새로운 파일로 저장합니다.
new_df.to_excel('compressed_data.xlsx', index=False)
