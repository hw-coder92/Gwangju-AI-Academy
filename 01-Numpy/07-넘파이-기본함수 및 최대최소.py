import numpy as np
arr = np.array([
                    [1, 2, 3], 
                    [0, 1, 4]
               ])

# 배열 전체에서 최소값 찾기
print(np.min(arr))
print(arr.min())

print(arr.min(axis=0)) # 열단위 최소값
print(arr.min(axis=1)) # 행단위 최소값

print(np.max(arr))
print(arr.max())

print(arr.max(axis=0)) # 열단위 최대값
print(arr.max(axis=1)) # 행단위 최대값

# 원소 합
print(np.sum(arr))
print(arr.sum())

print(arr.sum(axis=0)) 
print(arr.sum(axis=1))

# 누적합계
# cumulative sum 즉 누적 합계
# 앞에서부터 차례로 더한 값을 반환
print(np.cumsum(arr))
print(arr.cumsum())

# [[1 2 3]
#  [1 3 7]]
print(arr.cumsum(axis=0)) # 각 열에 대한 모든 행에서 동작
# [[1 3 6]
#  [0 1 5]]
print(arr.cumsum(axis=1)) # 각 행에 대한 모든 열에서 동작

# 평균/표준편차/중앙값

# 평균
print(np.mean(arr))
print(arr.mean())
print(arr.mean(axis=0))
print(arr.mean(axis=1))

# 표준편차
# 데이터가 평균으로부터 얼마나 퍼져있는지 측정하는 값
print(np.std(arr))
print(arr.std())
print(arr.std(axis=0))
print(arr.std(axis=1))

# 분산
print(np.var(arr))
print(arr.var())
print(arr.var(axis=0))
print(arr.var(axis=1))

# 중앙값
# [[1 2 3]
# [0 1 4]]
# ⁠1 2 3 0 1 4
#0 1 1 2 3 4

#중앙값은 정렬된 배열의 가운데 값입니다.
#원소 개수가 짝수(6개)이므로
#가운데 두 값의 평균 → (1 + 2) / 2 = 1.5
arr = np.array([
                    [1, 2, 3], 
                    [0, 1, 4]
               ])

print(arr)
print(np.median(arr))

# 행 기준
print(np.median(arr,axis=1))
# 열 기준
print(np.median(arr,axis=0))
