# Numpy 배열 생성
# 인덱싱
# 슬라이싱
# 벡터연산
# 통계
# 행렬연산
# 데이터 전처리

# 넘파이 특징
# 1. 모든 원소가 같은 자료형이어야 한다.
# 2. 원소의 갯수를 바꿀 수 없다.

import numpy as np

# 넘파이 생성
# 리스트에서 배열(numpy) 만들기
arr = np.array([1,2,3,4,5])
print(type(arr))
print(arr)
print(dir(arr))

# 모든 원소가 같은 자료형으로 통일시킴
arr = np.array([3.14,"안녕",2,4,3])
print(arr) # ['3.14''안녕''2''4''3']
print(type(arr))

arr = np.array([3.14,3,2,4,3])
print(arr) # [3.14 3.   2.   4.   3. ]
print(type(arr))

# 넘파이에서는 데이터 타입을 지정해 줄 수 있음
# 1. 정수형 (Integer)
# 타입    크기    범위
# int8    1 byte    -128 ~ 127
# uint8    1 byte    0 ~ 255
# int16    2 byte    -32,768 ~ 32,767
# uint16    2 byte    0 ~ 65,535
# int32    4 byte    -2,147,483,648 ~ 2,147,483,647
# uint32    4 byte    0 ~ 4,294,967,295
# int64    8 byte    -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807
# uint64    8 byte    0 ~ 18,446,744,073,709,551,615
# 2. 실수형 (Float)
# 타입    크기    대략적인 범위    정밀도
# float16    2 byte    ±6.5 × 10⁴    약 3자리
# float32    4 byte    ±3.4 × 10³⁸    약 7자리
# float64    8 byte    ±1.8 × 10³⁰⁸    약 15~16자리
# 일반 숫자 → int32
# 큰 정수 → int64
# 딥러닝 → float32
# 과학 계산 → float64
# 메모리 절약 → float16
# arr = np.array( [6,4,3], dtype='int32')
# print(arr)
# print(type(arr))

# 함수를 통한 배열 생성
# 0으로 채운 배열 생성
# arr = np.zeros(20)
# print(arr)

# arr = np.ones((3,5),dtype=int)
# print(arr)
# # [[1 1 1 1 1]
# #  [1 1 1 1 1]
# #  [1 1 1 1 1]]

# arr = np.full( (3,5,2),3.14) # 일반 수학(3행 5열 높이 2)과 달리 5행 2열이 3개
# print(arr)

# 선형대수
# Numpy는 스칼라, 벡터, 매트릭스(행렬) 개념을 다룸

# 1. 스칼라(Scalar)
# 하나의 숫자(크기만 있음)
# ex) 3, -1.5, π, 0, 100...

# 2. 벡터(Vector)
# 여러 개 숫자가 한 줄로 나열된 것(1차원)
# [10,20,30]

# 3. 매트릭스(Matrix, 행렬)
# 행과 열로 이루어진 2차원 배열
# [
#     [1,2,3]
#     [4,5,6]
# ]

# 그럼 3차원 이상은?
# 3차원 이상은 보통 텐서(Tenser)라 부른다.

# 0에서 시작해 2씩 더해 20까지 채우는 배열 생성
# [0 2 4 6 8 10 12 14 16 18]
arr = np.arange(0,20,2)
print(arr)

# 랜덤함수로 배열생성
# 0 과 1 사이의 숫자중에 실수 난수
# [[0.64334756 0.3906435  0.46174176]
#  [0.79529818 0.33663305 0.1577068 ]
#  [0.54854967 0.17326754 0.25468312]]
arr = np.random.random((3,3))
print(arr)
# 1부터 10사이
arr = np.random.randint(1,10,(3,3))
print(arr)

# 로또 번호 6개를 넘파이 배열로 뽑아내시오.
# replace = False
# 중복없이
lotto = np.random.choice(np.arange(1,46),size=6,replace=False)
print(lotto)

result = np.random.choice([10,20,30])
print(result)