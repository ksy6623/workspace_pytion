import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('car1.JPG',cv2.IMREAD_GRAYSCALE)

# 엣지 커널 3x3
kernel = np.array([
    [0,1,0]
    ,[1,-4,1]
    ,[0,1,0]
], dtype=np.float32)
edge_img = cv2.filter2D(img,ddepth=1,kernel=kernel)
plt.imshow(edge_img,cmap='gray')
plt.show()