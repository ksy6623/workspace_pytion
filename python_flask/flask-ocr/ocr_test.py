import cv2
import easyocr

reader = easyocr.Reader(['en','ko'],gpu=False)
results = reader.readtext('ko_en.png')
for results in results:
    print(results)

car_img = cv2.imread('car1.JPG')
car_reader = easyocr.Reader(['ko'])
car_results = car_reader.readtext(car_img)
for bbox, text, prob in car_results:
    print(bbox,text,prob)