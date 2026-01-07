# Agent Search Examples

This repo is a demonstration of how the PayeLink Agent Discovery (Agent Search)
SDK works end-to-end.

It includes:
- Mock organizations that expose discoverable agents via HTTP.
- A client agent that searches for and invokes other agents using the SDK.

## Repository layout
- `organization_a_agent/`: Mock org A exposing Currency Converter and Budget
  Planner agents plus their agent cards.
- `organization_b_agent/`: Mock org B exposing Meeting Scheduler and Note
  Summarizer agents plus their agent cards.
- `client_agent/`: Client agent that uses `payelink-agent-search` to discover
  agents and print results.

## Requirements
- Python 3.13+
- Optional: `uv` for dependency management (lockfiles are included)

## Setup
Each subproject is independent. Install dependencies in the folder you want to
run.

Using `uv`:
```bash
cd organization_a_agent
uv sync
```

Using `pip`:
```bash
cd organization_a_agent
python -m venv .venv
source .venv/bin/activate
pip install fastapi[standard] langchain langchain-openai langgraph langgraph-cli
```

Repeat for `organization_b_agent` or `client_agent` as needed.

## Run the agent servers
Organization A:
```bash
cd organization_a_agent
langgraph dev --port=2024
```

Organization B:
```bash
cd organization_b_agent
langgraph dev --port=2025
```

Once running, each service exposes:
- `/.well-known/*-agent-card.json` agent cards
- `/agents/public` list of public agents

## Run the client example
```bash
cd client_agent
python main.py
```

If the client needs API keys (for example, `OPENAI_API_KEY`) set them in your
environment before running.

