# 판다스는 2개의 객체 = 시리즈/데이터 프레임
# 시리즈 - 벡터(1차원)
# 데이터 프레임 - 매트릭스(2차원)
import pandas as pd
import numpy as np

arr = np.arange(100,105)
print(arr)

series = pd.Series(arr)
print(type(series))
print(series)
print(dir(series))

# 2차원 데이터 구조
# excel 문서의 시트와 유사
# 행 과 열 로 구성
# 각 열별로 데이터 타입을 가짐
# 시리즈 + 컬럼

# 모든 길은 로마로 통하듯이, 모든 데이터는 판다스로 통한다.
# 판다스 = 시리즈 객체 + 데이터프레임 객체

series = pd.Series(["사과","딸기"])
print(type(series))
print(series)
print(dir(series))

series = pd.Series(["사과",91,3.14])
print(type(series))
print(series)
print(dir(series))

data = {'a':100,'b':200}
series = pd.Series(data)
print(series)
# a    100       # a,b = index
# b    200
# dtype: int64