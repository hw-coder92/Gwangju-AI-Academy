from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI

load_dotenv()
from openai import OpenAI
client = OpenAI()

# 페르소나 => (인물설정)
# AI의 성격 + 경력 + 말투를 지정
# prompt = """
# [ROLE]
# 당신은 다음 특징을 가진 AI입니다.

# [Persona]
# - 20년차 여행 가이드
# - 매우 다정한 성격
# - 여행할때 효율적인 동선을 우선시함.
# - 핵심만 짧고 간단하게 설명

# [Task]
# 부산여행 2박 3일 일정을 계획하시오.

# [Constraint]
# - 5줄 이내
# - 비유 1개 포함
# - 초보자 대상
# """

# import sys
# from pathlib import Path
# import os

# sys.path.append(str(Path(__file__).resolve().parent.parent))
# from llm_loader import init_custom_llm

# print(init_custom_llm)

# llm = init_custom_llm()
# response = llm.invoke(prompt)

# print(response.content)

# prompt = """
# [ROLE]
# 당신은 다음 특징을 가진 AI입니다.

# [Persona]
# - 20년차 면접분석관
# - 매우 냉정한 성격
# - 회사에 입사하고자 하는 의지가 명확한 지원자를 선호함.
# - 핵심만 짧고 간단하게 설명하기를 좋아함.

# [Task]
# 본인이 맘에 들 정도인 지원자의 자기소개서를 작성하시오.

# [Constraint]
# - 7줄 이내
# - 비유 1개 포함
# """

# import sys
# from pathlib import Path
# import os

# sys.path.append(str(Path(__file__).resolve().parent.parent))
# from llm_loader import init_custom_llm

# print(init_custom_llm)

# llm = init_custom_llm()
# response = llm.invoke(prompt)

# print(response.content)


# 아래 PromptTemplate을 완성하시오.
import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm
from langchain_core.prompts import PromptTemplate

llm = init_custom_llm()

prompt = PromptTemplate.from_template(
    "안녕하세요. 저는 {name}이고 {job}입니다."
)

chain = prompt | llm

result = chain.invoke({
    "name" : ["Jason","John","Amanda"],
    "job" : ["Doctor","Salesman","Designer"]
})

print(result)