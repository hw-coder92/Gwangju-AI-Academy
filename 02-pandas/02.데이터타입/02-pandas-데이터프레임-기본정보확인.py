import pandas as pd
import numpy as np

data = {
    '이름' : ['유재석', '박명수', '정준하', '노홍철', '정형돈', '하하'],
    '지역' : ['서울', '부산', '부산', '서울', '서울', '서울'],
    '나이' : [19, 23, 20, 25, 18, 21],
    '국어점수' : [86, 90, 80, 65, 50, 60],
    '수학점수' : [86, 100, 66, 70, 40, 80],
    '코딩' : ['Python', 'Java', np.nan, 'Javascript', 'PYTHON', np.nan]
}

df = pd.DataFrame(data=data,index=['1번','2번','3번','4번','5번','6번'])
print(df)

# 데이터의 건강검진표

# df.info()는 Pandas에서 Dataframe의 전체적인 정보를 요약
# print(df.info())
# print(df.head(3))
print(df.tail())

# 기초통계량
# print(df.describe())

# print(df.count())
# print(df.min())
# print(df.max())

# print(df.sum())