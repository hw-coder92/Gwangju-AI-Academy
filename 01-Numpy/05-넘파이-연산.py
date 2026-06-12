# 넘파이 연산
# 행렬 연산을 기반으로 함
import numpy as np

arr1 = np.array([
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ])

arr2 = np.array([
                    [2, 2, 2],
                    [2, 2, 2],
                    [2, 2, 2]]
                )

print(arr1 + arr2)
print(arr1.__add__(arr2))
print(np.add(arr1,arr2))

print(arr1 - arr2)
print(np.subtract(arr1,arr2))

# * → 원소끼리 곱 (Element-wise)
# 즉 위치가 같은 값끼리 곱합니다.
# 기본적인 데이터 분석에서는 *
# @  → 행렬곱 (Matrix Multiplication)
# 수학에서의 행렬곱
# 변환, 계산, 예측(머신러닝, 딥러닝) = 선형대수
# 가중치 = 재료들을 섞어서 새로운 값 생성
print(arr1 * arr2)
print(np.multiply(arr1,arr2))

print(arr1 @ arr2)
print(np.matmul(arr1,arr2))

# 스칼라(상수)와의 곱
print(3 * arr1) # 브로드캐스팅
print(3 + arr1) # 

a = [1,2]
print(np.array(a)*3)