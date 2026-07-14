from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# class State(TypedDict):
#     score:int
#     result:str

# # node
# def check(state):
#     print("\n 점수검사", state["score"])
#     return state

# def pass_node(state):
#     state["result"]="합격"
#     return state

# def fail_node(state):
#     state["result"]="불합격"

# # 조건함수 = 분기
# def route(state):

#     if state["score"] >= 60:
#         return "pass"
    
#     return "fail"

# # 그래프 객체 생성
# builder = StateGraph(State)

# builder.add_node("check",check)
# builder.add_node("pass",pass_node)
# builder.add_node("fail",fail_node)

# builder.add_edge(START,"check")
# builder.add_conditional_edges(
#     "check",
#     route,
#     {
#         "pass":"pass",  # 분기함수, 조건함수
#         "fail":"fail"
#     }
# )
# builder.add_edge("fail",END)  
# builder.add_edge("pass",END)

# graph = builder.compile()

# # 실행

# result = graph.invoke({
#     "score":80
# })

# print(result)
# print(result["result"])

# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))

# from util import show_graph
# show_graph(graph)


class State(TypedDict):
    age:int
    result:str

# node
def check_age(state):
    print("\n 당신의 나이", state["age"])
    return state

def adult(state):
    state["result"]="성인"
    return state

def child(state):
    # state["result"]="미성년"
    return {
        "result":"미성년"
    }

# 조건함수 = 분기
def route(state):

    if state["age"] >= 20:
        return "adult"
    
    return "child"

# 그래프 객체 생성
builder = StateGraph(State)

builder.add_node("check_age",check_age)
builder.add_node("adult",adult)
builder.add_node("child",child)

builder.add_edge(START,"check_age")
builder.add_conditional_edges(
    "check_age",
    route,
    {
        "adult":"adult",  # 분기함수, 조건함수
        "child":"child"
    }
)
builder.add_edge("child",END)  
builder.add_edge("adult",END)

graph = builder.compile()

# 실행

result = graph.invoke({
    "age":20
})

print(result)
print(result["result"])

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from util import show_graph
show_graph(graph)