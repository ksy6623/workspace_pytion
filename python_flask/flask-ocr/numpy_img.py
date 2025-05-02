import cv2
import matplotlib.pyplot as plt
import numpy as np
from mpmath.libmp import normalize
from numpy.ma.core import resize

# pip install opencv-python
# pip install easyOCR
img = cv2.imread('car1.JPG')
print('원복 이미지:',img.shape)
print('픽셀[0,0]',img[0,0]) #[B, G ,R]
mean_pixel = np.mean(img, axis=(0,1))
print("RGB평균", mean_pixel)
# 원본 이미지(컬러)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# gray 이미지로
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imwrite('car1.JPG',gray)
#크기 조정
resized = cv2.resize(img, (128,128))
# 정규화(0~1 스케일로)
normalized = (resized/255.0).astype()
# gaussian blu
blurred = cv2.GaussianBlur(img, (5,5), 0)
# edge detection
edges = cv2.Canny(gray,100,200)
# 회전
(h,w) = img.shape[:2]
center = (w //2,h//2)
M = cv2.getRotationMatrix2D(center,15,1.0)
rotated = cv2.warpAffine(img,M,(w,h))
# 죄우 반전
flipped = cv2.flip(img,1)
images = [img_rgb, gray, resized, normalized, blurred, edges, rotated, flipped]
plt.figure(figsize=(15,10))
