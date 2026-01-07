from langchain.tools import tool
import httpx


@tool
def schedule_meeting(
    title: str,
    date: str,
    time: str,
    duration_minutes: int = 60,
    participants: list[str] = None,
    location: str = None
):
    """
    Use this tool to schedule a meeting.

    Args:
        title: The title or subject of the meeting
        date: The date of the meeting (format: YYYY-MM-DD)
        time: The time of the meeting (format: HH:MM in 24-hour format)
        duration_minutes: Duration of the meeting in minutes (default: 60)
        participants: List of participant email addresses or names (optional)
        location: Meeting location (optional, can be physical or virtual)

    Returns:
        A dictionary containing the meeting details and confirmation, or an error message if scheduling fails.
    """
    if participants is None:
        participants = []
    
    meeting_details = {
        "title": title,
        "date": date,
        "time": time,
        "duration_minutes": duration_minutes,
        "participants": participants,
        "location": location,
        "status": "scheduled",
        "meeting_id": f"MEET-{hash(f'{title}{date}{time}') % 1000000:06d}"
    }
    
    return {
        "success": True,
        "message": f"Meeting '{title}' has been scheduled for {date} at {time}",
        "meeting": meeting_details
    }


@tool
def task_tool(task: str) -> str:
    """
    Use this tool to delegate tasks to other agents when the user asks about anything outside your domain.

    This tool should be used when the user asks about topics other than meeting scheduling.
    The task will be routed to the appropriate specialized agent through the PayLink agent registry.

    Args:
        task: A clear description of the task or question that needs to be handled by another agent.

    Returns:
        The response from the delegated agent handling the task.
    """
    # Make a HTTP request to the PayLink agent registry to get available agents
    registry_url = "http://127.0.0.1:8000/api/v1/discover-agent"

    payload = {"task_request": task}

    try:
        with httpx.Client() as client:
            response = client.request("GET", registry_url, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        return f"Error delegating task: {e}"
