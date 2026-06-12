import pandas as pd
import numpy as np

# 딕셔너리로 생성시 자동으로 키가 시리즈의 인덱스로 들어감
series = pd.Series({'사과':1200,'딸기':3500, '키위':2100})
print(series)

# 속성확인
# Index(['사과', '딸기', '키위'], dtype='str')
print(series.index)
print(series.values)

# 넘파이 공통
print(series.dtype)
print(series.shape)
print(series.size)