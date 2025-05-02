from bs4 import BeautifulSoup
import requests
import csv
import os
import  urllib.request as req

csv_filename = 'cgv_chart.csv'
img_path = "./img"
# 폴더가 없으면 생성
if not os.path.exists(img_path):
    os.mkdir(img_path)

url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup.prettify())
ul = soup.select_one('.sect-movie-chart')
ols = ul.find_all('ol')
with open(csv_filename, mode='w',newline="",encoding='utf-8') as file:
    writer = csv.writer(file,delimiter='|')
    # 헤더추가
    writer.writerow(['제목','포스터','개봉일'])
    for ol in ols:
        lis = ol.find_all('li')
        for li in lis:
            title = li.select_one('.box-contents .title').text.strip()
            img_src = li.select_one('.thumb-image img')['src']
            release = li.select_one('.box-contents .txt-info strong').text.strip().replace('개봉','').strip()
            writer.writerow([title, img_src,release])
            img_file_path = os.path.join(img_path, title + '.png')
            req.urlretrieve(img_src, img_file_path)
print(f'csv 파일 {csv_filename} 저장 완료')