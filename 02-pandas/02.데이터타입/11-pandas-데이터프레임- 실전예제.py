import pandas as pd
import numpy as np

df_emp = pd.read_csv(r"C:\Users\user\Documents\Gwangju-AI-Academy\02-pandas\02.데이터타입\emp.csv")

df_emp.info()
print(df_emp.describe())
print(df_emp.head())

# 1번) 사원이름과 월급을 출력하시오.
print(df_emp[['ename','sal']])
print(df_emp.loc[ : , ['ename','sal']])
# 2번) 사원번호(empno), 이름(ename), 월급(sal), 직업(job)을 출력하시오.
print(df_emp[['empno','ename','sal','job']])
print(df_emp.loc[ : , ['empno','ename','sal','job']])
# 3번) 월급이 3000 이상인 사원들의 이름과 월급을 출력하시오.
print(df_emp[['ename','sal']][df_emp['sal']>=3000])
print(df_emp.loc[df_emp['sal']>=3000, ['ename','sal']]) # 추천
# 4번  직업이  SALESMAN 인 사원들의 이름과 월급과 직업을 출력하시오.
print(df_emp[['ename','sal','job']][df_emp['job']=='SALESMAN'])
print(df_emp.loc[df_emp['job']=='SALESMAN', ['ename','sal','job']])
# 5번 월급이 1000 에서 3000 사이인 사원들의 이름과 월급을 출력하시오 !
print(df_emp[['ename','sal']][df_emp['sal'].between(1000,3000)])
print(df_emp.loc[df_emp['sal'].between(1000,3000),['ename','sal']])
# 6번 sal이 가장 높은 사원의 이름과 급여를 출력하시오.
print(df_emp[['ename','sal']][df_emp['sal'] == df_emp['sal'].max()])
print(df_emp.loc[df_emp['sal']==df_emp['sal'].max(),['ename','sal']])
# 7번 부서번호별 평균 급여를 계산하시오.
print(df_emp.groupby('deptno')['sal'].mean().reset_index())
# print(df_emp.loc[df_emp.groupby('deptno')['sal'].mean(),['sal']])
# 8번 comm이 NULL인 사원들만 출력하시오. 또는 comm이 NULL인 아닌사원을 출력하시오.
print(df_emp[df_emp['comm'].isna()])
print(df_emp[df_emp['comm'].notna()])
# 9번 이름이 'SMITH'인 사원의 부서번호를 출력하시오.
print(df_emp[['deptno']][df_emp['ename']=='SMITH'])
print(df_emp.loc[['ename']=='SMITH',['deptno']])
#10번 매니저 번호가 같은 사원들끼리 묶어 부서번호별 평균 급여를 구하시오.
print(df_emp.groupby(['mgr','deptno'])['sal'].mean().reset_index())