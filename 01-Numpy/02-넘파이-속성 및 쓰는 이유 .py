import numpy as np
arr = np.random.randint(10,size=(3,4,5),dtype='int8')
# print(arr)

print(arr.ndim) # 차원확인
print(arr.shape) # 크기확인
print(arr.size) # 요소의 갯수 확인
print(arr.dtype) # 데이터 타입 확인

lst = [1, 2, 3, 4, 5]

result = []

for i in lst:
    result.append(i * 10)

print(result)

arr = np.array(lst) # 브로드캐스팅 - 넘파이를 쓰는 이유중 하나
print(arr * 10)