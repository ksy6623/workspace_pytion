import random
import requests

def get_lotto():
    """
     로또 번호 6개 생성
     1 ~ 45 사이의 숫자
    :return: set
    """
    lotto_num = set()
    while len(lotto_num) < 6:
        lotto_num.add(random.randint(1, 45))
    return lotto_num

def krw_to_usd(usd):
    url = "http://open.er-api.com/v6/latest/USD"
    res = requests.get(url)
    data = res.json()
    krw = data['rates']['KRW']
    return usd / krw
def usd_to_krw(usd):
    url = "http://open.er-api.com/v6/latest/USD"
    res = requests.get(url)
    data = res.json()
    krw = data['rates']['KRW']
    return usd * krw
# 원화 to 달러
# 달러 to 원화 함수를 만들어주세요
test = (1, 14, 15, 45)
# to list
test2 = list(test)[:2]  # :2 <--- 처음 부터 2-1 인덱스까지 슬라이싱
print(test2)
my_set = set(test2) # 해당 데이터가 포함 되어있는 set 생성
print(my_set, type(my_set))
# user_lotto 함수 생성
# input : 0 ~ n 개(사용자 희망 번호) 가변!?
# output:true or false,메세지,로또번호(사용자 희망 번호가 포함된)리턴 여러개!?
# 사용 입력 번호를 포함 시켜서 로또 번호 생성
# 단 사용자 입력은 최대 5개 까지만 포함 슬라이싱?!
# 각 사용자 입력은 1 ~ 45 사이 수만
# 조건을 만족 하지 않으면 false, 만족 하면 true
# 메세지는 false 일때 왜 false 인지

def user_lotto(*args):
    pass

# 모듈내 실행
if __name__ == '__main__':
    print("로또 잘 생성되나")
    print(get_lotto())
    print(f"달러 100은 : {usd_to_krw(100)}원")
    print(f"원화 20000은 : {krw_to_usd(20000)}달러")

    print(user_lotto(1, 2, 3, 4, 5, 6))#
    print(user_lotto(99, 2, 3))
    print(user_lotto())