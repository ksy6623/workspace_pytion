# 파일명: food_recommendation.py

import pandas as pd

# 1. CSV 파일 읽기
file_path = './전국통합식품영양성분정보표준데이터.csv'  # 파일명은 본인이 저장한 이름으로 맞춰주세요
data = pd.read_csv(file_path, encoding='cp949')

# 2. 열(column) 이름 확인
print("전체 컬럼 목록:")
print(data.columns.tolist())

# 3. 필요한 열만 추출
columns_needed = ['식품명', '에너지(kcal)', '탄수화물(g)', '단백질(g)', '지방(g)', '나트륨(mg)', '당류(g)', '식이섬유(g)']
food_data = data[columns_needed]

# 4. 확인: 추출한 데이터 샘플 보기
# print("\n필요한 열만 추출한 데이터:")
# print(food_data.head())

# 5. 사용자로부터 원하는 최대 열량 입력 받기
try:
    user_kcal = int(input("\n원하는 최대 열량(kcal)을 입력하세요: "))
except ValueError:
    print("숫자로 입력해주세요.")
    exit()

# 6. 입력받은 열량 이하 음식 필터링
filtered_food = food_data[food_data['에너지(kcal)'] <= user_kcal]

# [수정!] 먹을 수 없는 가공재료 제외 (누룽지는 제외 X)
keywords_to_exclude = ['전분', '분말', '농축', '액상', '농후']

for keyword in keywords_to_exclude:
    filtered_food = filtered_food[~filtered_food['식품명'].str.contains(keyword, na=False)]

# [중복 제거] 같은 음식명은 한 번만 남기기
filtered_food = filtered_food.drop_duplicates(subset='식품명')

# 7. 결과 출력
if not filtered_food.empty:
    print("\n[추천 가능한 음식 목록]")
    print(filtered_food[['식품명', '에너지(kcal)', '탄수화물(g)', '단백질(g)', '지방(g)', '나트륨(mg)', '당류(g)', '식이섬유(g)']])
else:
    print("조건에 맞는 음식이 없습니다.")



