from langchain.tools import tool, ToolRuntime

from payelink_agent_search import AgentSearchClient
from langgraph.types import Command, interrupt
from langchain.messages import ToolMessage


from typing import Literal

client = AgentSearchClient()


@tool
def task_tool(task: str, runtime: ToolRuntime) -> Command[Literal["select_agent"]]:
    """
    Use this tool to delegate tasks to other agents when the user asks about anything outside your domain.

    Args:
        task: A clear description of the task or question that needs to be handled by another agent.

    Returns:
        The response from the delegated agent handling the task.
    """

    response = client.search(query=task)

    if response.success:
        return Command(
            update={
                "found_agents": response.agents,
                "messages": [
                    ToolMessage(
                        content=f"Found call the select agent tool for user to select agent to use for task: {task}",
                        tool_call_id=runtime.tool_call_id,
                    )
                ],
            },
        )
    else:
        return Command(
            update={
                "messages": [
                    ToolMessage(
                        content=f"Error occurred while searching for agents: {response.error}",
                        tool_call_id=runtime.tool_call_id,
                    )
                ],
            },
        )


@tool
def select_agent(task: str, runtime: ToolRuntime) -> str:
    """
    This tool should be called immediately after the task_tool for user to select the agent they could like to use.

    Args:
        task: A clear description of the task or question that needs to be handled by another agent.

    Returns:
        The response from the selected agent handling the task.
    """

    found_agents = runtime.state.get("found_agents", [])

    # Pause execution and prompt user to select an agent
    response = interrupt(
        {
            "message": "Please select an agent from the following list to handle your task:",
            "agents": found_agents,
        }
    )
    
    # {"selected_agent": "agent_name"}
    # Example {"selected_agent": "Meeting Scheduler"}
    selected_agent = response.get("selected_agent")
    
    for agent in found_agents:
        if agent.agent_name == selected_agent:
            final_selected_agent = agent

    print(f"Final selected agent: {final_selected_agent}")
    return Command(
        update={
            "found_agents": [],
            "selected_agent": final_selected_agent,
            "messages": [
                ToolMessage(
                    content=f"Delegated task to agent: {final_selected_agent.agent_name}",
                    tool_call_id=runtime.tool_call_id,
                )
            ],
        },
    )
