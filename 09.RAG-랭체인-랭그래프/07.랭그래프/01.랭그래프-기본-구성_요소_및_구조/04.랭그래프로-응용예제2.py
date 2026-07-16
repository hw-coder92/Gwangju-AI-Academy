from typing import TypedDict
from langgraph.graph import StateGraph, START, END

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

# 1. state 정의
class State(TypedDict):
    price: int

# 2. 노드 함수 만들기
def discount(state:State):
    # state["price"] = int(state["price"] * 0.9)
    return {
        "price": int(state["price"] * 0.9)   
    }

def delivery(state:State):
    # state["price"] = state["price"] + 5000
    return {
        "price": state["price"] + 5000    
    }

# 3. graph 객체 생성
builder = StateGraph(State)

builder.add_node("discount",discount)
builder.add_node("delivery",delivery)

builder.add_edge(START,"discount")
builder.add_edge("discount","delivery")
builder.add_edge("delivery",END)

# 4. 컴파일
graph = builder.compile()

# 5. 실행
result = graph.invoke({
    "price":100000
})
print(result)
print(result["price"])

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from util import show_graph
show_graph(graph)