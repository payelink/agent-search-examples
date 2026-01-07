from payelink_agent_search import AgentSearchClient


client = AgentSearchClient()

response = client.search(
    query="Currency",
    # max_result=2,
    # country="kenya",
    # capability="streaming",
    # default_input_mode=["text/plain"],
    # default_output_mode=["text/plain"],
)

if response.success:
    for idx, agent in enumerate(response.agents, start=1):
        print(f"\n{'=' * 40}")
        print(f"Agent {idx}")
        print(f"{'=' * 40}")

        print(f"Name            : {agent.agent_name}")
        print(f"Description     : {agent.agent_description}")
        print(f"URL             : {agent.agent_url}")
        print(f"Organization    : {agent.organization_name}")
        print(f"Org URL         : {agent.organization_url}")
