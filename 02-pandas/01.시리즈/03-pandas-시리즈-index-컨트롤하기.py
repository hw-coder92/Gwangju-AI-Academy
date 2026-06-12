import pandas as pd
import numpy as np

# 딕셔너리로 생성시 자동으로 키가 시리즈의 인덱스로 들어감
series = pd.Series({'사과':1200,'딸기':3500, '키위':2100})
#print(series)

series.name = "과일가격"
print(series)

# 인덱스 수정
# 인덱스 수정은 전체수정가능, 일부 부분 수정불가
#series.index[0] = '오렌지' (x)
series.index = ['오렌지','딸기','참외']
print(series)

# 인덱스 삭제
# 인덱스 삭제는 불가능하며, 초기화 가능
series = series.reset_index(drop=True)
print(series)