from typing import Literal

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from pydantic import BaseModel

from src.budget_planner.tool import plan_budget, summarize_expenses
from src.budget_planner.prompt import AGENT_B_PROMPT


llm = init_chat_model(model="claude-haiku-4-5-20251001", temperature=0.0)


class ResponseFormat(BaseModel):
    """Respond to the user in this format."""

    status: Literal["input_required", "completed", "error"] = "input_required"
    message: str


agent = create_agent(
    model=llm,
    tools=[plan_budget, summarize_expenses],
    system_prompt=AGENT_B_PROMPT,
)


