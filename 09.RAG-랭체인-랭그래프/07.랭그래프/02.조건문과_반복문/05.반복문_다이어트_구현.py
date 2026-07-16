# 체중 감량
# 그래프
#         START
#           │
#           ▼
#      diet
#           │
#  weight > 65
#      ┌────┴────┐
#      ▼         ▼
#    diet       END
# 초기값
# weight = 70
# 결과
# 65
# State
# class State(TypedDict):
#     weight: int
# 조건
# 한 번 반복할 때마다 1kg 감량
# 65kg이 되면 종료

from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    weight:int

# node
def diet(state):
    print(f"현재체중 {state["weight"]}kg")

    return {
        "weight":state["weight"] - 1
    }

# 분기 함수
def check_weight(state):
    
    if state["weight"] <=65:
        return "end"
    else:
        return "continue"
    
# 그래프 객체 생성
builder = StateGraph(State)

builder.add_node("diet",diet)

builder.add_edge(START,"diet")

builder.add_conditional_edges(
    "diet",
    check_weight,
    {
        "continue":"diet",
        "end":END
    }
)

graph = builder.compile()

# 실행

result = graph.invoke({
    "weight":70
})

print(result)
print(result["weight"])

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from util import show_graph
show_graph(graph)