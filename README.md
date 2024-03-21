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
│  │      geocoding-naver-api-csv-ver.py
│  │      get_agexl.py
│  │      model_prediction.py
│  │      xl_test.py
```

- src : 페이지구성, 기능구현<br>
- src/tool : 데이터 전처리에 사용한 파일들<br>
tool 주요 파일<br>
geocoding-api-xlver (주소->경도 위도 좌표 변환 naver api 이용)<br>
model_prediction<br> (Linear regression을 이용한 예측값 생성)<br>
check_nan (전처리 후 xlsx파일 검사)

# 사용한 데이터

www.molit.go.kr


국토교통부_실거래가 정보<br>
https://www.data.go.kr/data/15004246/fileData.do


국토교통부_실거래가 정보<br>
https://www.data.go.kr/data/3050988/fileData.do


소상공인시장진흥공단_상가(상권)정보<br>
https://www.data.go.kr/data/15083033/fileData.do



# 마무리 하며
하나의 프로젝트를 위해 4일이라는 시간은 정말 짧은 것 같다.<br>
하지만 컴퓨터 공학과에서 습득한 가장 중요한것 중 한가지가 어떻게든 기간 안에 끝내기인 것 같고, 그 기억으로 마무리를 했다.<br>
streamlit을 사용해 간편하게 ui를 구성하기는 했지만 기능구현, 많은 양의 데이터 전처리, ui구성까지 작업하여 욕심만큼 구현하지 못해 아쉬운 마음이 크다..<br>
#### 아쉬운점
- 7가지 매매 (아파트, 연다세대, 단다가구, 오피스텔, 분양권, 상업업무용, 토지) 중 아파트 데이터만 사용했다<br>
- 구현한 기능의 융합<br>
여러개의 페이지를 구성하기 보다는 관련된 구현 기능을 하나의 페이지에 일목요연하게 정리하고 싶었는데, 그게 쉽지 않았다.<br>
페이지 정리를 잘 하지 못해 오히려 사용하기 불편하다고 생각이 들었고, 너무 많은 데이터로 인해 속도가 너무 느렸으며 해결하지 못한 에러가 자꾸 나서 페이지를 분할 시키는 것으로 롤백을 여러번 했다..<br>
- 예외처리 부족<br>
오류가 났던 부분만 처리를 해 주었다.. 사실은 전체적인 예외처리를 어떻게 해야하는 지 모르겠다. 내가 돌리다가 오류가 나서 디버깅 하고 데이터 타입을 바꾸는 부분을 추가하는 등의 방식이 아니라 오류가 발생해도 프로그램이 돌아가지만 내가 오류 메세지를 확인할 수 있도록 설계하는 것이 이상적인 방법이라고 생각했다. 이건 코드를 많이 읽어 보지 않아서 발생한 문제인 것 같다. 실력자들의 코드를 많이 읽어보자.
#### 문제발생과 해결
- 대한민국의 주소 체계가 이렇게 복잡하다는 것을 처음 알게 되었다. 지번주소 / 도로명주소 / 법정동 / 행정동 등 필요한 데이터를 구하고 나서도 전처리에 시간을 굉장히 많이 사용했다.
주소값 대략 8만개, 상권 정보 30만개, 지역별 성별/나이 데이터 400개<br>
연관되어 있는 자료들을 법정동으로 묶기도 하고, 행정동으로 묶기도 하고, 경도와 위도를 사용하기도 하여 여러가지 파일을 사용하는 조금 지저분한 방식으로 해결을 했다.<br>
시간적 여유가 있다면 데이터 처리에 조금 더 신경을 써서 k-fold 교차검증 모델을 사용했다면 정확도가 많이 올라가지 않았을까 생각한다.<br>
- 많은 양의 데이터를 사용할 때 속도도 큰 문제였다.<br>
그래프로 시각화 할때는 문제가 되지 않았는데 지도에 많은 정보를 표시할 때 문제가 생겼다<br>
streamlit 캐싱을 엑셀 파일을 읽는 함수에 적용해 페이지에 다시 접근할 때 시간을 단축시켰지만 지도를 표시하고 움직일때도 버벅이는 모습을 보여 marker cluster를 사용해 해결했다.<br>
하지만 근본적으로 마커를 심는 시간이 오래 걸렸기 때문에 표시 후 움직임은 해결 되었지만 생성 시간을 줄이기 위해서는 지도의 zoom값, 즉 화면에 표시되는 구역의 마커를 먼저 심고 zoom을 당겼을 때 새로고침 버튼을 눌러 로드하는 방식을 채택해야 할 것 같다. 이 부분은 추후 업데이트 해 보아야 겠다.
