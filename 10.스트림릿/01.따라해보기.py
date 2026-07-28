import streamlit as st
import pandas as pd

# python -m streamlit run 파일명.py => 스트림릿 구동

# UI  = 화면 구성 및 User 동작 포함(버튼을 누르는 동작 등등...)

# 서버 = 다수를 기다리는 쪽 = ServerSocket + while True + 쓰레드 = 그룹채팅


# HTML
# CSS
# 부트스트랩
# 자바스크립트 : 언어

# Front 프레임워크  :  React, Vue ,Angular ......


# BackEnd 프레임워크 : 
#     파이썬 기반: Django, FastAPI , Flask ,
#     자바 기반 : Spring

# python -m pip install --force-reinstall streamlit

####################################################
# 제목
####################################################
st.title("스트림릿 따라하기 : 허쌤")
st.header("Header 예제")
st.subheader("SubHeader 예제")


st.text("안녕하세요")
st.write("Streamlit을 배워봅시다!")

# ####################################################
# # Markdown
# ####################################################

st.markdown("---")
st.markdown("### Markdown")
st.markdown("## Markdown")
st.markdown("# Markdown")
st.markdown("""
- Python
- Streamlit
- LangChain
- RAG
""")
# ####################################################
# # 코드 출력
# ####################################################

st.markdown("---")
st.subheader("코드 출력")

code = """
for i in range(5):
    print(i)
"""

st.code(code,language="python")

# ####################################################
# # 캡션
# ####################################################

st.caption("이 화면은 스트림릿 실습입니다.")

# ####################################################
# # 이미지
# ####################################################

st.markdown("---")
st.subheader("이미지 출력")

st.image("cat.png",width=300)


# ####################################################
# # DataFrame
# ####################################################

st.markdown("---")
st.subheader("데이타 프레임 출력")

df = pd.DataFrame(
    {
        "이름": ["홍길동", "김철수", "이영희"],
        "나이": [20, 22, 25],
        "점수": [90, 85, 100]
    }
)

st.dataframe(df)

# ####################################################
# # Table
# ####################################################

st.subheader("테이블(Table)")
st.table(df)

# ####################################################
# # Metric
# ####################################################

st.markdown("---")
st.subheader("Metric")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("매출","100만원","+10%")

with col2:
    st.metric("매출","100만원","+10%")

with col3:
    st.metric("매출","100만원","+10%")

st.markdown("---")
st.subheader("Columns(컬럼 함수)")

left, right = st.columns(2)

with left:
    st.write("왼쪽 화면")
    st.success("성공")

with right:
    st.write("오른 화면")
    st.info("정보")

# ####################################################
# # Container
# ####################################################

st.markdown("---")
st.subheader("Expander")

with st.expander("클릭하면 내용이 열립니다."):
    st.write("숨겨진 내용입니다.")
    st.write("여러 줄도 가능합니다.")

# ####################################################
# # Sidebar
# ####################################################
st.sidebar.title("사이드 바")
st.sidebar.write("여기는 메뉴 영역입니다.")
st.sidebar.success("스트림릿")

# ####################################################
# # 메시지 박스
# ####################################################
st.markdown("---")

st.success("성공 메시지")
st.warning("경고 메시지")
st.error("오류 메시지")
st.info("정보 메시지")

# ####################################################
# # 끝
# ####################################################

st.markdown("---")

st.write("오늘 수업 끝!")