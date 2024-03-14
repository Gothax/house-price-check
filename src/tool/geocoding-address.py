import csv
from geopy.geocoders import Nominatim
geo_local = Nominatim(user_agent='South Korea')

"""
데이터 전처리
streamlit 페이지 구성과 관계없는 파일
페이지 로딩시간 단축을 위해 data폴더의 주소에 경도, 위도값을 추가
"""
from tqdm import tqdm


# geopy를 이용해 경도, 위도로 변환
# 생성 속도를 높이기 위해 캐시 사용
def geocoding(address):
    cache = {}  # 캐시 저장소

    if address in cache:
        return cache[address]
    else:
        try:
            geo = geo_local.geocode(address)
            x_y = [geo.latitude, geo.longitude]
            cache[address] = x_y  # 변환 결과를 캐시에 저장
            return x_y

        except:
            return [0, 0]


def add_geolocation_to_file(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    for row in tqdm(data, desc="진행 중"):  # tqdm을 사용하여 진행 상황을 표시합니다.
        address = row[1] + ' ' + row[2]
        geolocation = geocoding(address)
        row.extend(geolocation)

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("위도와 경도 정보가 추가된 파일이 생성되었습니다.")


input_file = "data/아파트(매매)_실거래가_20240314104119.csv"  # 입력 파일명
# input_file = "data/test.csv"  # 입력 파일명
output_file = "data/output_withlat.csv"  # 출력 파일명

add_geolocation_to_file(input_file, output_file)


