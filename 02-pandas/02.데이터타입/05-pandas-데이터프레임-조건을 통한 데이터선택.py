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
print(df.info())

# 불리언 인덱싱
# 나이가 20살보다 큰 사람정보를 뽑아내시오.
print(df[df["나이"]>20])
print(df["나이"]>20)
# 나이가 20살 이하인 사람정보를 뽑아내시오.
print(df[(df["나이"]<=20)])
print(df[~(df["나이"]>20)]) # ~ : ~가 아니다.
# 수학점수가 70점 이상인 데이터들을 뽑아내시오.
print(df[df["수학점수"]>=70])

# loc 활용하기
print(df.loc[df['수학점수']>= 70])
print(df[df['수학점수']>= 70],["수학점수","지역"])
# 지역이 부산이고 나이가 20살 이상
print(df.loc[(df['나이']>= 20)&(df['지역'] == "부산")])
# 나이가 20살 이상 또는 코딩이 Python인 사람
# print(df.loc[(df['나이']>= 20),(df['코딩'] == "Python")])
print(df.loc[(df['코딩'].str.upper() == "PYTHON")])
