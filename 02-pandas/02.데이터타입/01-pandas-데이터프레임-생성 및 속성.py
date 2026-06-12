# 2차원 데이터 구조 (3차원 이상은 numpy로 가능)
# excel 문서의 시트와 유사, RDBMS 테이블과 유사
# 행 과 열로 구성
# 각 행렬로 데이터 타입을 가짐
# 시리즈 + 컬럼

import pandas as pd
import numpy as np

df = pd.DataFrame([     # 데이터프레임 작성시 df 로 쓰는게 사회적약속
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(df)

df = pd.DataFrame(np.array([    
    [1,2,3],
    [4,5,6],
    [7,8,9]
]), columns= ['가','나','다'],index=['a','b','c'])
print(df)

# 딕셔너리를 통한 생성
data = {
    '이름': ['김철수', '이영희', '홍길동'], 
    '학교': ['서울고', '대전고', '경기고'], 
    '점수': [80, 95, 85]
}

df = pd.DataFrame(data)
print(df) # print(df.T) = 행과 열 바꿈

# 데이터 프레임 속성확인 # 데이터 프레임은 index/columns/values 3개가 합쳐진 것.
print(df.index)
print(df.columns)
print(df.values)

print(df.shape)
print(df.ndim)
print(df.size) # 요소의 갯수 확인
#print(df.dtype) # 데이터 타입 확인

# 인덱스 수정(단독 수정불가)
df.index = ['1번','2번','3번']
print(df)
print(df.index)