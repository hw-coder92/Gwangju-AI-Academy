import numpy as np
arr = np.random.randint(10,size=10)
# 원본을 바꿈 => arr.sort()
# print(arr.sort())
# print(arr) # 원본 값을 바꿈

# 원본에 영향을 주지 않는다.
print(np.sort(arr))
print(arr)

# 내림차순
print(np.sort(arr)[::-1])
arr2 = np.sort(arr)[::-1]
print(arr2)

np.random.seed(42)
# 2차원 배열 정렬
arr = np.random.randint(15,size=(3,4))
print(arr)
# 행단위 정렬
print(np.sort(arr,axis=1))
# 열단위 정렬
print(np.sort(arr,axis=0))