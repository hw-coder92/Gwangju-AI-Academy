import pandas as pd
import numpy as np

data = {
    '이름' : ['유재석', '박명수', '정준하', '노홍철', '정형돈', '하하'],
    '지역' : ['서울', '부산', '부산', '서울', '서울', '서울'],
    '나이' : [19, 23, 20, 25, 18, 21],
    '국어점수' : [86, 90, 80, 65, 50, 60],
    '수학점수' : [86, 100, 66, 70, 40, 80],
    '코딩' : ['Python', 'Java', np.nan, 'Javascript', 'PYTHON', np.nan],
    '전공' : ['문과', '이과', '이과', '이과', '문과', '문과'], 
}

df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번'])
print(df)

# 결측치 체크
# print(df.info())
# print(df.isnull().sum())

# # 데이터프레임의 '지역' 컬럼 내 데이터들을 모두 결측치로 지정
# df['지역'] = np.nan
# print(df)
# #fillna 를 통해 결측치 값을 바꿈
df.fillna("없음",inplace=True)
print(df)

# # 특정 열 지정하여 처리하기
# df["지역"].fillna('없음', inplace=True)
# print(df)
# # 삭제
# # NaN을 가진 모든 행 삭제
# df.dropna(inplace=True)
# print(df)

# 결측치 처리(대체) 방법
# 1. 평균
# 2. 최빈값 = 
# 3. 해당 컬럼 삭제
# 4. 최대, 최소값
# 5. 중앙값
# 6. 이전값으로 채우기 또는 다음값으로 채우기