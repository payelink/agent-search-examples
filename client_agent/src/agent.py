from langchain.agents import create_agent, AgentState
from langchain.chat_models import init_chat_model

from src.prompt import AGENT_PROMPT
from src.tools import task_tool
from src.tools import select_agent


class CustomState(AgentState):
    found_agents: list[dict] = []
    selected_agent: dict = {}


llm = init_chat_model(model="claude-haiku-4-5-20251001")



agent = create_agent(
    model=llm,
    tools=[task_tool, select_agent],
    system_prompt=AGENT_PROMPT,
    state_schema=CustomState,
)
