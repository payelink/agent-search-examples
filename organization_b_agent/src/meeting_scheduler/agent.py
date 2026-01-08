
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

from src.meeting_scheduler.tool import schedule_meeting, task_tool
from src.meeting_scheduler.prompt import AGENT_B_PROMPT



llm = init_chat_model(model="claude-haiku-4-5-20251001", temperature=0.0)


agent = create_agent(
    model=llm,
    tools=[schedule_meeting, task_tool],
    system_prompt=AGENT_B_PROMPT
)
