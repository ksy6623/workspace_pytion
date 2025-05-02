import pandas as pd
import random

# 데이터 읽기
file_path = '전국통합식품영양성분정보표준데이터.csv'
data = pd.read_csv(file_path, encoding='cp949')

# 필요한 열만 추리기
columns_needed = ['식품명', '에너지(kcal)', '탄수화물(g)', '단백질(g)', '지방(g)', '나트륨(mg)', '당류(g)', '식이섬유(g)']
food_data = data[columns_needed]

# 평범한 음식 리스트
common_foods = ['닭가슴살', '고구마', '흰쌀밥', '삶은계란', '시금치', '브로콜리', '된장국', '두부', '김치', '오이', '상추']

# 사용자 입력
try:
    user_kcal = int(input("\n원하는 최대 열량(kcal)을 입력하세요: "))
except ValueError:
    print("숫자로 입력해주세요.")
    exit()

# 조건에 맞는 음식 필터링
filtered_food = food_data[
    (food_data['에너지(kcal)'] <= user_kcal) &
    (food_data['식품명'].apply(lambda x: any(item in x for item in common_foods)))
]

# 중복 제거
filtered_food = filtered_food.drop_duplicates(subset='식품명')

# 식단 조합 추천
if not filtered_food.empty:
    print("\n[추천 식단 조합]")
    for i in range(3):  # 세트 3개 추천
        recommend = filtered_food.sample(n=2)
        total_kcal = recommend['에너지(kcal)'].sum()

        print(f"\n- 추천 세트 {i+1} (총 {total_kcal:.1f} kcal)")
        print(recommend[['식품명', '에너지(kcal)', '탄수화물(g)', '단백질(g)', '지방(g)']])
else:
    print("조건에 맞는 평범한 음식이 없습니다.")
