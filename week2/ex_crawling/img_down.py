import  urllib.request as req

url = 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000089/89058/89058_320.jpg'
req.urlretrieve(url, 'test.png')