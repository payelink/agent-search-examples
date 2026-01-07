from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()


@app.get("/.well-known/currency-converter-agent-card")
def read_currency_converter_agent_card():
    """
    Agent card for the Currency Converter agent.
    """
    return FileResponse(".well-known/currency-converter-agent-card.json")


@app.get("/.well-known/budget-planner-agent-card")
def read_budget_planner_agent_card():
    """
    Agent card for the Budget Planner agent.
    """
    return FileResponse(".well-known/budget-planner-agent-card.json")


@app.get("/agents/public")
def list_public_agents():
    """
    Return a list of publicly available agents exposed by this service.
    """
    agents = [
        {
            "id": "currency_converter",
            "name": "Currency Converter",
            "description": "A specialized assistant for currency conversions and exchange rate queries.",
            "card_url": "/.well-known/currency-converter-agent-card",
        },
        {
            "id": "budget_planner",
            "name": "Budget Planner",
            "description": "Helps users plan monthly budgets, categorize expenses, and set savings goals.",
            "card_url": "/.well-known/budget-planner-agent-card",
        },
    ]
    return JSONResponse(content={"agents": agents})
