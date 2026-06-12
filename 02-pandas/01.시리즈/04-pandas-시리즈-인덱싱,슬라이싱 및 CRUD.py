import pandas as pd
import numpy as np

# 딕셔너리로 생성시 자동으로 키가 시리즈의 인덱스로 들어감
series = pd.Series({'사과':1200,'딸기':3500, '키위':2100})
print(series)

# 단일값 접근
print(series['사과'])
print(series['딸기'])

# 결과값이 시리즈 타입(객체)으로 리턴됨
print(series[['딸기','사과']]) # 팬시 인덱싱 - 위치지정

# 과일 중에 2000원 이상 과일을 시리즈로 뽑아내시오.
# 조건 필터링을 통한 접근(불린 인덱싱) => 시리즈도 넘파이처럼 불린 인덱싱이 지원됨
print(series[series > 2000]) # 시리즈로 뽑아줌

# 행번호 인덱싱
# print(series[1:3])
# print(series[0]) # 단일값
# print(series[:])

# 인덱스 기반 인덱싱
# print(series['사과','딸기'])
# print(series['사과':'딸기'])

# iloc 함수 활용 = integer = 행번호 기반
print(series.iloc[0:3]) # 함수
print(series.iloc[1:3]) # 함수

# 특정 위치에 있는 값 가져오기
print(series.iloc[0])

# 시리즈 추가
# 없으면 추가, 있으면 업데이트
# 인덱스 이름으로
series.loc['바나나'] = 5000
print(series)

series['참외'] = 6000
print(series)

# 업데이트
#
series['참외'] = 7000
print(series)

series.iloc[-1] = 9000
print(series)

# 삭제
#series.drop('사과',inplace=True) # 원본 내 삭제(inplace = 원본 수정)
#print(series)

series_2 = series.drop('사과') # 원본유지 삭제
print(series_2)

series.drop(['딸기','바나나'],inplace=True)
print(series)