import pandas as pd

# 병합된 파일을 불러옵니다.
merged_df = pd.read_excel('merged_file_with_predictions.xlsx')

# 각 열에 대해 NaN 값이 있는지 확인합니다.
nan_check = merged_df.isnull().any()

# NaN 값이 있는 모든 열을 출력합니다.
print("NaN 값을 포함하는 열:")
print(nan_check[nan_check == True])

# 전체 데이터 프레임에서 NaN 값의 개수를 확인합니다.
total_nan = merged_df.isnull().sum().sum()
print(f"전체 데이터 프레임에서 NaN 값의 총 개수: {total_nan}")

# NaN 값을 포함하는 행을 확인하고 싶다면 아래 코드를 사용합니다.
if total_nan > 0:
    print("NaN 값을 포함하는 행들:")
    print(merged_df[merged_df.isnull().any(axis=1)])
