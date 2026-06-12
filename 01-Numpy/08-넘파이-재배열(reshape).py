import numpy as np
arr = np.arange(12)
print(arr)

arr.reshape(3,4)
print(arr) # 원본은 바꾸지 않음

# 이 차원은 네가 알아서 계산해줘
arr.reshape(-1,4)
arr.reshape(2,-1)

arr = np.array([
                    [1, 2, 3], 
                    [0, 1, 4]
               ])

arr.flatten() # 1차원 배열로 만드는 함수