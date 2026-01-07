from langchain.tools import tool
import httpx


@tool
def get_exchange_rate(
    from_currency: str = "USD", to_currency: str = "EUR", date: str = "latest"
):
    """
    Use this tool to get the current exchange rate for a given currency pair.

    Args:
        from_currency: The currency to convert from (default: USD)
        to_currency: The currency to convert to (default: EUR)
        date: The date for the exchange rate (default: latest)

    Returns:
        A dictionary containing the exchange rate data, or an error message if the request fails.
    """
    try:
        response = httpx.get(
            f"https://api.frankfurter.app/{date}",
            params={"from": from_currency, "to": to_currency},
            timeout=30.0,
        )
        response.raise_for_status()

        data = response.json()

        if "rates" not in data:
            return {"error": "Invalid API response format"}

        return data
    except httpx.TimeoutException as e:
        return {"error": f"Request timed out after 30 seconds: {e}"}
    except httpx.HTTPError as e:
        return f"Error: {e}"


@tool
def task_tool(task: str) -> str:
    """
    Use this tool to delegate tasks to other agents when the user asks about anything outside your domain.

    This tool should be used when the user asks about topics other than currency conversion or exchange rates.
    The task will be routed to the appropriate specialized agent through the PayLink agent registry.

    Args:
        task: A clear description of the task or question that needs to be handled by another agent.

    Returns:
        The response from the delegated agent handling the task.
    """
    # Make a HTTP request to the PayLink agent registry to get available agents
    registry_url = "http://127.0.0.1:8000/api/v1/discover-agent/"

    payload = {
        "query": task,
        "wallet_connection_string": "pl_conn_live_N7-W3MPWKRsCglomv92qfw",
    }

    try:
        with httpx.Client(timeout=300.0) as client:
            response = client.request("POST", registry_url, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.TimeoutException as e:
        return f"Error delegating task: Request timed out after 300 seconds. {e}"
    except httpx.HTTPError as e:
        return f"Error delegating task: {e}"
