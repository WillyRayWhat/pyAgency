"""
tests for the agents.agent.Agent class
"""

from src.agents.agent import Agent


# Agents have self-incrementing id numbers and report their 'names' as
# 'Agent <id>'
def test_agent_id():
    """Test auto-incrementing agent ids"""
    agent = Agent()
    assert agent.agent_id == 0
    assert agent.get_name() == "Agent 0"
    agent = Agent()
    agent = Agent()
    assert agent.agent_id == 2
