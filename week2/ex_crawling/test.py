from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
url = 'https://www.kyobobook.co.kr/'
driver.get(url)
time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')
book_list = soup.select('#topicAll .swiper-slide')
for book in book_list:
    title = book.select_one('.prod_name').text.strip()
    if "The Scent of Page" in title:
        continue
    author = book.select_one('.prod_author').text.strip()
    link = book.select_one('.prod_link')['href']
    print(title, author, link)
    print("=" * 100)
driver.quit()

