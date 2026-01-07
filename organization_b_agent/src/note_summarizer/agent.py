from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

from src.note_summarizer.prompt import NOTE_SUMMARIZER_PROMPT
from src.note_summarizer.tool import summarize_text, extract_action_items
from pydantic import BaseModel
from typing import Literal


llm = init_chat_model(model="gpt-4o-mini", temperature=0.0)


class ResponseFormat(BaseModel):
    """Respond to the user in this format."""
    status: Literal['input_required', 'completed', 'error'] = 'input_required'
    message: str


agent = create_agent(
    model=llm,
    tools=[summarize_text, extract_action_items],
    system_prompt=NOTE_SUMMARIZER_PROMPT,
)


