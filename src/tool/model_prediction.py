import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


################################ 데이터 불러오기
data = pd.read_excel('merged_file.xlsx')  # price 데이터 파일 경로를 적절히 수정해주세요.
data['price'] = data['price'].str.lstrip()
data['price'] = data['price'].str.replace(',', '')  # 쉼표(,) 제거
data['price'] = data['price'].astype(float)

# 입력 변수와 타겟 변수 분리
# X = data[['특징1', '특징2', '특징3']]  # 입력 변수에 해당하는 특징들을 선택해주세요.
X = data[['전용면적(㎡)', '건축년도', '교육', '보건의료', '음식', '예술·스포츠']]  # 입력 변수에 해당하는 특징들을 선택해주세요.
y = data['price']  # 예측하려는 타겟 변수를 선택해주세요.
####################################################




# 학습 데이터와 테스트 데이터로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 선형 회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 테스트 데이터로 예측 수행
y_pred = model.predict(X_test)

# 전체 데이터셋을 사용한 집값 예측
y_all_pred = model.predict(X)

# 예측 결과를 원본 데이터프레임에 '예측 집값'이라는 새로운 열로 추가
data['예측 집값'] = y_all_pred

# 결과 확인
# print(data.head())

# 필요하다면, 예측 결과가 추가된 데이터프레임을 새로운 파일로 저장
# data.to_excel('merged_file_with_predictions.xlsx', index=False)

# 모델 평가
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# print("Mean Squared Error:", mse)
# print("R-squared:", r2)

