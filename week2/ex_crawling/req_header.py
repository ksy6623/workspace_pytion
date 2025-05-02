import requests

url = "https://www.oxfordlearnersdictionaries.com/definition/english/address_1?q=address"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)
print(res.status_code)