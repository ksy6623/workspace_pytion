import csv
import requests
from bs4 import BeautifulSoup

def get_paxnset(page):
    url = "https://www.paxnet.co.kr/tbbs/list?tbbsType=L&id=N10841&page=1"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    div = soup.select_one('#comm-list')
    lis = div.find_all('li')
    deta_rows = []
    for i, li in enumerate(lis):
        if i != 0:
            seq = li.select_one('.type')
            if seq:
                seq_num = seq.get('data-seq')  # 존재하면 가져오기
                title = li.select_one('.title .best-title').text.strip()
                deta_rows.append([seq_num, title])
    with open('paxnet.csv','a',encoding='utf-8',newline='')as f:
        write = csv.writer(f,delimiter='|')
        write.writerow(deta_rows)

if __name__ == '__main__':
    for p in range(1,11):
        get_paxnset(p)
