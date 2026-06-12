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

# 정렬
print(df.sort_index(ascending=False)) # 내림차순(ascending=False), 오름차순(ascending=True, 디폴트)
# 컬럼 기준
print(df.sort_values('나이',ascending=True))
# 이름 오름차순으로 정렬하시오.
print(df.sort_values('이름'))
# 두 개를 기준으로 적용하기
# 지역과 나이순으로 정렬하시오.
print(df.sort_values(['지역','나이']))
print(df.sort_values(['지역','나이'],ascending=[True,False])) # 지역은 오름차순, 나이는 내림차순
# 수학점수가 높은 순으로 정렬하고, 동일한 점수일 경우 이름을 기준으로 오름차순 정렬하라.
print(df.sort_values(["수학점수","이름"],ascending=[False,True]))

# 함수 적용 - apply
# 데이터 전처리 과정에서 특정 열이나 행을 변환해야 할 때가 있음
# apply() 함수를 데이터를 적용

def add_s(age):
    return str(age) + "세"

print(type(df['나이']))
df['나이'] = df['나이'].apply(add_s)
# df['나이'] = str(df['나이'])+"세" (X)
print(df)
# 나이에서 '세' 제거하고 정수형으로 변환
def remove_s(age_str):
    return int(str(age_str).replace("세",""))

df['나이'] = df['나이'].apply(remove_s)
print(df)

# 국어점수와 수학점수을 더해서 평균을 구하고, 평균 컬럼으로 저장하시오.
df["평균"] = (df["국어점수"] + df["수학점수"])/2
print(df)
# 등급 컬럼에 # 평균이 90점 이상 A, 80점 이상 B, 70점 이상 C, 나머지 F
def grade(score):

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

df["등급"] = df["평균"].apply(grade)
print(df)