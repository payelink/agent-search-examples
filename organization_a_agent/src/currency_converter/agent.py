
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

from src.currency_converter.tool import get_exchange_rate, task_tool
from src.currency_converter.prompt import AGENT_A_PROMPT
from pydantic import BaseModel
from typing import Literal


llm = init_chat_model(model="claude-haiku-4-5-20251001", temperature=0.0)



class ResponseFormat(BaseModel):
    """Respond to the user in this format."""
    status: Literal['input_required', 'completed', 'error'] = 'input_required'
    message: str


agent = create_agent(
    model=llm,
    tools=[get_exchange_rate, task_tool],
    system_prompt=AGENT_A_PROMPT
)
