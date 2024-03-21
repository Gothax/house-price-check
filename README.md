# house-price-check
can check reasonable price of house in seoul

data by Ministry of Land, Infrastructure and Transport

# 어살?
어디살고싶어?

### 어살의 다른점
- 정확히 얼마에 거래 되었는지, 5년간의 데이터를 모두 볼 수 있습니다

![스크린샷 2024-03-19 095815](https://github.com/Gothax/house-price-check/assets/82752784/b724aa90-56ab-4687-81c1-9c29cb401ee0)

![스크린샷 2024-03-19 100316](https://github.com/Gothax/house-price-check/assets/82752784/7b07f5b1-df03-4138-8242-ae18b0c6afad)

<img src="https://github.com/Gothax/house-price-check/assets/82752784/da2dfac6-4a40-4d11-9351-37c94cf8b7f9" width="400"/>


# 기능
- 지도상에서 볼 수 있는 최근 1년간 모든 아파트 매매의 실거래가
 ![스크린샷 2024-03-19 033504](https://github.com/Gothax/house-price-check/assets/82752784/021b5645-e8b2-494b-84d7-0ff07c1010ef)
- 2020 ~ 2024 서울 집값 추이 (동네단위로 확인 가능) <br>
  월별로 비교
  
![스크린샷 2024-03-15 173233](https://github.com/Gothax/house-price-check/assets/82752784/97b7ffad-8640-4fc3-a6b2-e200381940cd)

- 상권 분석 <br>
  법정동 기준으로 구역을 나누어서 지도에 표시했고, 동네에 상가 업종별 개수를 파악할 수 있습니다

  ![스크린샷 2024-03-19 001034](https://github.com/Gothax/house-price-check/assets/82752784/687c19f3-57e5-49cd-a44c-451f511b7ffc)
  
- 동네별 연령대, 성별 분포 확인 <br>
matplotlib에서 한글이 깨지는 문제는 글꼴 설치 후 재부팅했을 때 해결 되었습니다
  
![스크린샷 2024-03-19 005524](https://github.com/Gothax/house-price-check/assets/82752784/2495c831-1028-4e7b-ae9c-5794dec890d7)

- 미래 가격 예측 (Beta) <br>
k-fold 교차검증을 사용했을 때 성능이 너무 떨어져서 간단하게 진행하기 위해 Linear regression을 채택했습니다. <br>
 
![스크린샷 2024-03-19 023201](https://github.com/Gothax/house-price-check/assets/82752784/adb9c904-9a10-4cbb-b5cf-3d716fc8f15f)

![스크린샷 2024-03-19 023336](https://github.com/Gothax/house-price-check/assets/82752784/93d135d4-2107-4bb5-a77c-5d1f79ed7ec6)

전용면적(㎡)', 건축년도, 교육(분야의 상가 개수), 보건의료(분야의 상가 개수), 음식(분야의 상가 개수), 예술·스포츠(분야의 상가 개수) <br>
총 6개의 데이터를 지표로 사용했습니다. <br>
초기 계획은 boston 예제의 데이터셋과 비슷한 형태로 크롤링을 통해 방개수, 지역 범죄율등을 포함시키려 했지만<br>
프로젝트 기간 4일동안 데이터를 모으고 가공하는데 무리가 있어 정확도가 많이 떨어졌습니다..<br>

모델 평가값

Mean Squared Error: 3252893561.6222425 <br>
R-squared: 0.5101828861644071 <br>


# 디렉토리

```
│  .env
│  .gitignore
│  LICENSE
│  README.md
├─src
│  │  age_gender.py
│  │  business_district.py
│  │  compare_price.py
│  │  home.py
│  │  main.py
│  │  predict_price.py
│  │  transaction_price_map.py
│  │
│  ├─tool
│  │      check_nan.py
│  │      geocoding-address.py
│  │      geocoding-api-xlver.py
│  │      geocoding-naver-api-csv-ver.p은 단축시켰지만 지도를 표시하고 움직일때도 버벅이는 모습을 보여 marker cluster를 사용해 해결했다.<br>
하지만 근본적으로 마커를 심는 시간이 오래 걸렸기 때문에 표시 후 움직임은 해결 되었지만 생성 시간을 줄이기 위해서는 지도의 zoom값, 즉 화면에 표시되는 구역의 마커를 먼저 심고 zoom을 당겼을 때 새로고침 버튼을 눌러 로드하는 방식을 채택해야 할 것 같다. 이 부분은 추후 업데이트 해 보아야 겠다.

