import numpy as np

# 배열과 차이점.
arr = [1,2,3,4]
print('arr:',arr)
print('arr type',type(arr))

numpy_arr = np.array(arr)
print(f"ndarry shape 배열의 모양(행,열,채널,..등):{numpy_arr.shape}")
print(f"dtype 자료형 :{numpy_arr.dtype}")
print(f"dim 차원 수 : {numpy_arr.ndim}")
print(f" numpy:{numpy_arr}")

numpy_2d = np.array([[1,2,3,4],[5,6,7,8]])
print(f"ndarry shape 배열의 모양(행,열,채널,..등):{numpy_2d.shape}")
print(f"dtype 자료형 :{numpy_2d.dtype}")
print(f"dim 차원 수 : {numpy_2d.ndim}")
print(f" numpy:{numpy_2d}")

numpy_3d = np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]])
print(f"ndarry shape 배열의 모양(행,열,채널,..등):{numpy_3d.shape}")
print(f"dtype 자료형 :{numpy_3d.dtype}")
print(f"dim 차원 수 : {numpy_3d.ndim}")
print(f" numpy:{numpy_3d}")

numpy_4d = np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]])
print(f"ndarry shape 배열의 모양(행,열,채널,..등):{numpy_4d.shape}")
print(f"dtype 자료형 :{numpy_4d.dtype}")
print(f"dim 차원 수 : {numpy_4d.ndim}")
print(f" numpy:{numpy_4d}")

data1 = np.array([[1,2],[3,4]])
data2 = np.array([[0,1],[1,0]])
print(data1)
print(data2)
# dot product 행렬곱
data3 = np.dot(data1,data2)
print(data3)
# 전치 행렬
data4 = np.transpose(data3)
print(data4)
# 형태 변경
test = np.arange(10)
print(test)
print(test.shape,test.dtype,test.ndim)
print('2 x 5',test.reshape(2,5))
print('5 x 2',test.reshape(5,2))
print('1d',test.reshape(-1,1))