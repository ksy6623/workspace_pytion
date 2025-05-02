import requests
# 없다면 pip install requests
# HTTP 요청을 쉽게 할 수 있는 라이브러리
# get, post, put, delete 요청 처리
# 응답: json or text
# 요청 시 자동으로 URL 인코딩 처리
# HTTP 요청 중 발생할 수 있는 오류에 대한 예외 처리 제공

url = "https://api.upbit.com/v1/market/all"
res = requests.get(url)
if res.status_code == 200:
    data = res.json()
    for v in data:
        print(f"마켓명:{v['market']} 코인명:{v['korean_name']}")

def fn_get_coin_price(code):
    """
    예(https://api.upbit.com/v1/ticker?markets=KRW-BTC)
    요청하여 코인 trade_price를 리턴하는 함수
    :param code: 코인 마켓코드
    :return: price : 실시간 거래가격
    """
    url = f"https://api.upbit.com/v1/ticker?markets={code}"
    res = requests.get(url)
    price = 0
    if res.status_code == 200:
        data = res.json()
        price = data[0]['trade_price']
    return price
print(fn_get_coin_price("KRW-BTC"))
print(fn_get_coin_price("KRW_ETH"))