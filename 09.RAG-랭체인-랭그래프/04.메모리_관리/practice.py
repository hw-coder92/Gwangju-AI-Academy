# 아래 코드를 완성하시오.

# 사용자의 질문과 AI의 답변을 저장하도록 작성하시오.

from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

from langchain_core.chat_history import ChatMessageHistory

history = ChatMessageHistory()

history.add_user_message("안녕하세요")

history.add_ai_message("안녕하세요. 무엇을 도와드릴까요?")

print(history.messages)

# 조건

# ChatMessageHistory 사용
# 사용자 메시지 저장
# AI 메시지 저장
