import pandas as pd
import random

# 파일 읽기
data = pd.read_csv('정리된_식품데이터_국수정.csv', encoding='cp949')

# 주식, 부식, 디저트, 소스 나누기
main_foods = data[data['분류'] == '주식']
side_foods = data[data['분류'] == '부식']
desserts = data[data['분류'] == '디저트']
sauces = data[data['분류'] == '소스']

# 밀키트/간편식 키워드 리스트
brand_keywords = [
    '워커힐', '이순미', '풀무원', 'CJ', '삼양', '오뚜기', '롯데', '농심',
    '자연드림', '컵밥', '비비고', '간편식', '햇반', '이마트', 'GS', '홈플러스'
]

# 추천 모드 선택
mode = input("\n추천 모드를 선택하세요 (1: 밀키트 포함 / 2: 요리 가능한 식품만): ").strip()

# 요리 모드 선택 시 브랜드/간편식 제품 제외
if mode == '2':
    filter_pattern = '|'.join(brand_keywords)
    main_foods = main_foods[~main_foods['식품명'].str.contains(filter_pattern, na=False)]
    side_foods = side_foods[~side_foods['식품명'].str.contains(filter_pattern, na=False)]
    desserts = desserts[~desserts['식품명'].str.contains(filter_pattern, na=False)]

# 사용자 최대 열량 입력
try:
    user_kcal = int(input("\n원하는 최대 열량(kcal)을 입력하세요: "))
except ValueError:
    print("숫자로 입력해주세요.")
    exit()

# 주식 1개 추천
recommend_main = main_foods.sample(n=1)

# 부식 1~2개 추천
side_n = random.choice([1, 2])
recommend_side = side_foods.sample(n=side_n)

# 식단 조합
recommend_meal = pd.concat([recommend_main, recommend_side])

# 총 열량 계산
total_kcal = recommend_meal['에너지(kcal)'].sum()

print("\n[오늘의 추천 식사]")
print(recommend_meal[['식품명', '에너지(kcal)', '탄수화물(g)', '단백질(g)', '지방(g)', '분류']])
print(f"\n총 식사 열량: {total_kcal:.1f} kcal")

# 디저트 추천 여부
remain_kcal = user_kcal - total_kcal

if remain_kcal > 50:
    dessert_choice = input(f"\n남은 열량 {remain_kcal:.1f}kcal로 디저트를 추천받을까요? (y/n): ").lower()
    if dessert_choice == 'y':
        available_desserts = desserts[desserts['에너지(kcal)'] <= remain_kcal]
        if not available_desserts.empty:
            recommend_dessert = available_desserts.sample(n=1)
            print("\n[추천 디저트]")
            print(recommend_dessert[['식품명', '에너지(kcal)', '탄수화물(g)', '단백질(g)', '지방(g)']])
        else:
            print("남은 열량으로 추천할 수 있는 디저트가 없습니다.")
else:
    print("\n남은 열량이 적어 디저트 추천은 생략합니다.")
