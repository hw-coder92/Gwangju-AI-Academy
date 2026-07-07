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
# JSON 출력
{{
    "제목":"",
    "내용":""
}}

질문:
{topic}
"""
)

# msg = prompt.invoke({
#     "topic":"AI Agent"
# })

# print(msg)

# 출력이 스트링으로 뽑아서
output_parser = StrOutputParser()
# output_parser = JsonOutputParser()
# output_parser = XMLOutputParser() # XML 출력

chain = prompt | llm | output_parser

result = chain.invoke({
    "topic":"AI의 미래는?"
})

print(result)

# chain =  prompt | llm 

# result = chain.invoke({
#     "topic":"반복문"
# })
# print(result.content)