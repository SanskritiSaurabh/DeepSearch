from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents.research_agent import ResearchAgent
from agents.answer_drafter import AnswerDrafter
from utils.config import get_config

config = get_config()

class AgentState(TypedDict):
    query: str
    research_data: str
    final_answer: str

def research_node(state):
    agent = ResearchAgent(config)
    results = agent.run(state["query"])
    return {"research_data": results}

def drafting_node(state):
    drafter = AnswerDrafter(config)
    answer = drafter.run(state["research_data"], state["query"])
    return {"final_answer": answer}

# Build the workflow
workflow = StateGraph(AgentState)
workflow.add_node("research", research_node)
workflow.add_node("draft", drafting_node)
workflow.set_entry_point("research")
workflow.add_edge("research", "draft")
workflow.add_edge("draft", END)
app = workflow.compile()