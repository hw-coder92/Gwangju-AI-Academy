from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 실습 문제

# 문제:

# START
#  ↓
# plus10
#  ↓
# minus5
#  ↓
# END

# 초기값:
# 100
# 결과:
# 105

# 1. 스테이트 설계
# 랭그래프용 변수 선언
class State(TypedDict):
    value: int

# 2. 노드 함수 만들기
def plus10(state:State):
    # state["value"] = state["value"] + 10
    return {
        "value": state["value"] + 10    
    }

def minus5(state:State):
    # state["value"] = state["value"] - 5
    return {
        "value": state["value"] - 5    
    }

# 3. graph 객체 생성
builder = StateGraph(State)

builder.add_node("plus10",plus10)
builder.add_node("minus5",minus5)

builder.add_edge(START,"plus10")
builder.add_edge("plus10","minus5")
builder.add_edge("minus5",END)

# 컴파일
graph = builder.compile()

# 실행
result = graph.invoke({
    "value":100
})
print(result)
print(result["value"])

# 숫자 계산기

# 그래프
# START
#   ↓
# multiply2
#   ↓
# plus20
#   ↓
# END

# 초기값
# 50
# 결과
# 120

# (50 × 2 = 100 → +20 = 120)

class State(TypedDict):
    value: int

# 2. 노드 함수 만들기
def multiply2(state:State):
    # state["value"] = state["value"] * 2
    return {
        "value": state["value"] * 2   
    }

def plus20(state:State):
    # state["value"] = state["value"] + 20
    return {
        "value": state["value"] + 20    
    }

# 3. graph 객체 생성
builder = StateGraph(State)

builder.add_node("multiply2",multiply2)
builder.add_node("plus20",plus20)

builder.add_edge(START,"multiply2")
builder.add_edge("multiply2","plus20")
builder.add_edge("plus20",END)

# 컴파일
graph = builder.compile()

# 실행
result = graph.invoke({
    "value":50
})
print(result)
print(result["value"])

# 쇼핑 금액 계산 프로그램을 랭그래프로 완성하시오.
# 그래프
# START
#   ↓
# discount
#   ↓
# delivery
#   ↓
# END
# 초기값
# 100000
# 결과
# 95000

# 계산 과정

# 100000
# ↓

# 10% 할인

# 90000
# ↓

# 배송비 +5000

# 95000

class State(TypedDict):
    value: int

# 2. 노드 함수 만들기
def discount(state:State):
    # state["value"] = int(state["value"] * 0.9)
    return {
        "value": int(state["value"] * 0.9)   
    }

def delivery(state:State):
    # state["value"] = state["value"] + 5000
    return {
        "value": state["value"] + 5000    
    }

# 3. graph 객체 생성
builder = StateGraph(State)

builder.add_node("discount",discount)
builder.add_node("delivery",delivery)

builder.add_edge(START,"discount")
builder.add_edge("discount","delivery")
builder.add_edge("delivery",END)

# 컴파일
graph = builder.compile()

# 실행
result = graph.invoke({
    "value":100000
})
print(result)
print(result["value"])