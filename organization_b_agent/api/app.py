from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()

@app.get("/.well-known/meeting-scheduler-agent-card")
def read_agent_card():
    return FileResponse(".well-known/meeting-scheduler-agent-card.json")


@app.get("/.well-known/note-summarizer-agent-card")
def read_note_summarizer_agent_card():
    return FileResponse(".well-known/note-summarizer-agent-card.json")


@app.get("/agents/public")
def list_public_agents():
    """
    Return a list of publicly available agents exposed by this service.
    """
    agents = [
        {
            "id": "meeting_scheduler",
            "name": "Meeting Scheduler",
            "description": "A specialized assistant for scheduling meetings.",
            "card_url": "/.well-known/meeting-scheduler-agent-card",
        },
        {
            "id": "note_summarizer",
            "name": "Note Summarizer",
            "description": "Summarizes notes, extracts key points, and lists action items.",
            "card_url": "/.well-known/note-summarizer-agent-card",
        },
    ]
    return JSONResponse(content={"agents": agents})