# 아래 코드를 완성하시오.
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm
# 템플릿 사용
from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser,JsonOutputParser,XMLOutputParser

llm = init_custom_llm()

prompt = ChatPromptTemplate.from_template(
"""

{{
    "제목":"",
    "내용":""
}}

질문:
{topic}
"""
)

# output_parser = StrOutputParser()

# chain = prompt | llm | output_parser

# result = chain.invoke({
#     "topic":"AI"
# })

# print(result)

# 조건

# 문자열(String)로 출력되도록 한다.

# 코딩을 완성하시오.

# 아래 코드가 JSON 형태로 출력되도록 완성하시오.

# from langchain_core.output_parsers import JsonOutputParser

# output_parser = JsonOutputParser()

# chain = prompt | llm | output_parser

# result = chain.invoke({
#     "topic":"머신러닝"
# })

# print(result)

# 조건

# JsonOutputParser 사용

# 아래 코드를 완성하시오.

# JSON 형식으로 출력되도록 Prompt를 완성하시오.

# from langchain_core.prompts import ChatPromptTemplate

# prompt = ChatPromptTemplate.from_template(
# """
# {{
#     "제목":"",
#     "내용":""
# }}

# 질문:

# {topic}

# """
# )

# output_parser = JsonOutputParser()

# chain = prompt | llm | output_parser

# result = chain.invoke({
#     "topic":"AI의 미래"
# })

# print(result)

# 조건

# JSON 형식 출력
# 제목(title)
# 내용(content)

# 아래 코드가 실행되도록 완성하시오.

# 출력 결과

{
    "title":"Python",
    "content":"Python은 프로그래밍 언어입니다."
}
from langchain_core.output_parsers import JsonOutputParser

prompt = ChatPromptTemplate.from_template(
"""
JSON 출력
{{
    "제목":"",
    "내용":""
}}
질문
{topic}
"""
)

parser = JsonOutputParser()

chain = prompt | llm | parser

result = chain.invoke({
    "topic":"Python"
})

print(result)

# 조건

# JsonOutputParser 사용
# JSON 출력
