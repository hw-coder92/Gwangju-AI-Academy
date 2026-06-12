import numpy as np
arr =  np.array([10, 20, 30, 40, 50])
print(arr)

# 30보다 큰 값만 뽑아 내시오.
# for value in arr:
# if value > 30:
# print(value)
# 그런데 넘파이 배열 에서는 for문을 돌리면 왕따 당함
# for 문 안돌리려고 numpy 배열 쓰는 거임 ㅋㅋㅋ

condition = arr > 30
print(condition) #[False False False  True  True]
result = arr[condition] # = result = arr[[False, False, False,  True,  True]]
print(result)
print(arr[arr>30])

# 조건: 짝수만 선택
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr[arr % 2 == 0]) # [ 2 4 6 8 10]

# 1부터 1000까지의 배열을 만들고 그 중에서 7의 배수이자 11의 배수인 숫자들만 뽑아내시오.
# [ 77 154 231 308 385 462 539 616 693 770 847 924]
arr = np.arange(1,1001)
# NumPy 배열 연산에서는 | & (파이프 기호) 
# 파이썬 기본 문법은 and or
print(arr[ (arr % 7 == 0) & (arr % 11 ==0) ])
# 1부터 1000까지의 배열을 만들고 그 중에서 7의 배수이거나 또는 11의 배수인 숫자들만 뽑아내시오.
print(arr[ (arr % 7 == 0) | (arr % 11 ==0) ])
# 1부터 1000까지의 배열에서 짝수이면서 100의 배수
print(arr[(arr % 2 == 0) & (arr % 100 ==0)])

#팬시 인덱싱
import numpy as np

arr = np.array([10,20,30,40,50])

print(arr[2])

# 일반 인덱싱 → 하나 선택
# 슬라이싱 → 연속 선택
# 팬시 인덱싱 → 원하는 위치 여러 개 선택

# Fancy Indexing(팬시 인덱싱)은 인덱스로 리스트나 배열을 전달해서 원하는 위치의 값들을 한 번에 선택하는 방식 
print(arr[ [0,2,4] ])
print(arr[ [4,1,3] ])
print(arr[ [1,1,1] ])

# 불린 인덱싱과 팬시 인덱싱의 차이
# 불린 인덱싱 조건 arr > 30 조건선택
# 펜시 인덱싱 위치선택 arr[[0,2]] 위치선택

import numpy as np

scores = np.array([
    [80,90,100],
    [70,60,80],
    [95,85,90]

])

print(scores[ [0,2] ])
print(scores[ : , [0,2] ])

import numpy as np

arr = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [90,100,110,120],
    [130,140,150,160]
])

# 첫 번째 행 전체를 출력하시오.
print(arr[0])
# 세 번째 열 전체를 출력하시오.
print(arr[:,[2]])
# 마지막 두 행만 추출하시오.
print(arr[2:])

# 매출 데이터 중 30000 이상만 추출하시오.

sales = np.array([
    12000,
    45000,
    38000,
    15000,
    50000
])
print(sales[sales >=30000])

#학생 평균이 80 이상인 학생만 추출하시오.

scores = np.array([
    [80,90,70],
    [60,65,50],
    [95,85,90],
    [70,75,80]
])

# 조건

# 행 평균 >= 80
scores = np.array(scores)
row_means = np.mean(scores, axis=1)
indices = np.where(row_means >= 80)[0]
result = scores[indices]
print(result)

# 음수만 추출하시오.

data = np.array([
    -10, 30, -20,
    50, -60, 90
])
print(data[data<0])
