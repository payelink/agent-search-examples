# Agent Search Examples

A minimal end-to-end demo of the PayeLink Agent Discovery (Agent Search) SDK.

This repo shows how discoverable agents can be published by organizations and how a client agent can discover and invoke them.

What’s included
- organization_a_agent/: Mock organization A exposing Currency Converter and Budget Planner agents + agent cards.
- organization_b_agent/: Mock organization B exposing Meeting Scheduler and Note Summarizer agents + agent cards.
- client_agent/: Example client that uses `payelink-agent-search` to discover agents and invoke them.

Repository layout
- organization_a_agent/: FastAPI/langgraph mock service; exposes agent cards and a public agents list.
- organization_b_agent/: Same as above for a second org.
- client_agent/: Example Python client demonstrating discovery and usage.

Requirements
- Python 3.13+
- Optional: uv (used here for dependency/lockfile management)
- Optional: OpenAI or other model API key if client uses external LLMs (set as env var)

Quick setup
Each subproject is independent. Install only where you will run things.

With uv:
```bash
cd organization_a_agent
uv sync
```

With pip (example):
```bash
cd organization_a_agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# or: pip install fastapi[standard] langchain langchain-openai langgraph langgraph-cli
```

Run the mock org servers
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

Exposed endpoints (once running)
- /.well-known/*-agent-card.json — agent card metadata (one per agent)
- /agents/public — JSON list of public agents the org publishes

Run the client
```bash
cd client_agent
python main.py
```
If the client requires API keys (e.g., OPENAI_API_KEY), export them in your shell before running:
```bash
export OPENAI_API_KEY="sk-..."
```

Environment variables
- OPENAI_API_KEY — optional, required if the client or agents call OpenAI.
- Any other env var referenced in each subproject's README or .env example.

Testing and development notes
- Each org service is independent; you can run one or both.
- Agent cards follow the discoverable metadata shape used by Agent Search — check /.well-known/*-agent-card.json for examples.
- The client demonstrates discovery via the /agents/public endpoint and then fetches agent cards.

Troubleshooting
- Port conflicts: choose different ports for langgraph dev.
- Missing deps: ensure virtualenv is activated and requirements installed.
- API key errors: verify env vars are exported in the shell where you run the client.

Contributing
- Add example agents under the appropriate org folder.
- Keep agent card metadata consistent with the discovery schema used by the client.

License
- See LICENSE (if present) for repo license details.

