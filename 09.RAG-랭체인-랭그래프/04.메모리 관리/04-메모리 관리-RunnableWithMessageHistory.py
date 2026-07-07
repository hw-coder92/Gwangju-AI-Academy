#  메모리 관리에서 가장 중요한 부분
# **"왜 RunnableWithMessageHistory를 사용하는가?"**를 이해하는 것이 목표
# 흐름은 반드시 아래처럼 진행하는 것을 추천
# 직접 저장 → 불편함 → RunnableWithMessageHistory → 자동 저장

# 예제 1. 직접 저장하는 방식 (복습)

# history.add_user_message(question)
# response = llm.invoke(history.messages)
# history.add_ai_message(response.content)

# 질문
# "매번 이 세 줄을 써야 할까요?"
# 답
# 너무 불편하다.

# (직접 저장)
# 사용자
#    ↓
# add_user_message()
#    ↓
# LLM
#    ↓
# add_ai_message()

# 사용자
#    ↓
# RunnableWithMessageHistory
#    ↓
# 자동 저장
#    ↓
# LLM
#    ↓
# 자동 저장

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
import sys
from pathlib import Path
import os
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

####################################################
# 1. LLM 객체 생성
####################################################
llm = init_custom_llm()

####################################################
# 2. Prompt 생성
####################################################
prompt = ChatPromptTemplate.from_messages([
    ("system","당신은 친절한 AI 입니다."),
    MessagesPlaceholder("history"), # 이전 대화 기록을 저장하는 위치
    ("human","{question}") # 질문 저장
])

####################################################
# 3. Chain 생성
####################################################
chain = prompt | llm

history = InMemoryChatMessageHistory()
# history = [
# HumanMessage(content='내 이름은 철수야', additional_kwargs={}, response_metadata={}), 
# ]

####################################################
# 4. Memory 저장소
####################################################
store = {}

def get_session_history(session_id):
    
    if session_id not in store:
        print(f"새로운 메모리 생성:{session_id}")
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]

####################################################
# 5. RunnableWithMessageHistory 객체 생성
####################################################
chain_with_history = RunnableWithMessageHistory(
    runnable = chain,
    get_session_history = get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

####################################################
# 6. 대화 함수
####################################################
def chat(session_id, question):

    response = chain_with_history.invoke(
        {"question":question},
        config={
            "configurable":{
                "session_id":session_id
            }
        }
    )
    print("응답:",response.content)
    print()

####################################################
# 7. 첫 번째 사용자
####################################################

chat("abc","안녕하세요")
chat("abc","제 이름은 철수 입니다.")
chat("abc","제 이름은 뭐였죠")

for message in store["abc"].messages:
    print(message)

####################################################
# 8. 두 번째 사용자
####################################################

chat("abc","안녕하세요")
chat("abc","제 이름은 철수 입니다.")
chat("abc","제 이름은 뭐였죠")

for message in store["abc"].messages:
    print(message)