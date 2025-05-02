import  random

# 업다운 게임
# 3번의 기회
# 사용자 입력이 맞으면 '정답', 작으면 '업', 크면 '다운' 출력
# 틀릴 때마다 몇번의 기회가 있는 지 출력
# computer의 랜덤 값은 1 ~ 10 사이의 정수

num = random.randint(1,10)
cht= 3

while cht > 0:
    use = int(input("1 ~ 10사이의 정수를 입력하세요!"))
    if use == num:
        print("정답입니다")
        break
    elif use < num:
        print("업!!")
    else:
        print("다운!!")
        break
    cht -= 1
    if cht != 0:
        print("남은 기회:",cht)
    else:
        print(f"게임종료 정답은 + {num}")