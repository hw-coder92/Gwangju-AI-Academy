# 데이터 시각화
# 데이터 시각화를 위해서는 우선 데이터의 종류를 먼저 이해하는 것이 중요

# 1. 수치형 데이터 => 사칙연산 가능
#  - 연속형 실수형태 (키, 몸무게)
#  - 이산형 정수형태 (A반 학생수, 인원수)

# 2. 범주형 데이터 => 사칙연산 불가
#  - 순서형 순서있음 학점, 설문조사 점수
#  - 명목형 순서없음 성별, 우편번호

# 명목형 → 막대그래프, 파이차트, Countplot
# 순서형 → 정렬된 막대그래프
# 수치형 → 히스토그램, 박스플롯

# ============================================================================

# 막대 → 선 → 히스토그램 → 박스플롯 → 산점도 → 히트맵 순서로 이해
# 실무에서 가장 많이 쓰는 TOP 10
# 막대그래프 → 비교
# 선그래프 → 추세
# 산점도 → 관계
# 히스토그램 → 분포
# 박스플롯 → 이상치
# 히트맵 → 상관관계
# 누적막대 → 구성비
# 파이차트 → 비율
# 트리맵 → 계층
# 산점도 + 회귀선 → 예측
# 한 줄 규칙
# 비교 → 막대 (범주(카테고리)끼리 크기를 비교)
# 변화 → 선
# 관계 → 산점도
# 분포 → 히스토그램
# 비율 → 파이
# 상관 → 히트맵
# 자주 쓰는 plt
# | 코드              | 의미    |
# | --------------- | ----- |
# | plt.figure()  | 그림 생성 |
# | plt.plot()    | 선그래프  |
# | plt.bar()     | 막대그래프 |
# | plt.scatter() | 산점도   |
# | plt.hist()    | 히스토그램 |
# | plt.pie()     | 파이차트  |
# | plt.title()   | 제목    |
# | plt.xlabel()  | x축    |
# | plt.ylabel()  | y축    |
# | plt.grid()    | 격자    |
# | plt.show()    | 출력    |

import matplotlib.pyplot as plt

# 가장 간단한 선 그리기
plt.plot([1,2,3])
print(plt.plot)

dept = ["개발","기획","마케팅","디자인"]
count = [50,30,20,10]

plt.figure(figsize=(3,2))
plt.bar(dept,count)
print(plt.bar)

import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

!apt-get -qq install fonts-nanum

font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"

fm.fontManager.addfont(font_path)

font_name = fm.FontProperties(fname=font_path).get_name()

plt.rc("font", family=font_name)
plt.rcParams["axes.unicode_minus"] = False