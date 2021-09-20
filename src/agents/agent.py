"""
Base agent class
"""
from .abstract_agent import AbstractAgent


class Agent(AbstractAgent):
    """
    First concrete agent class.  Others will likely extend this.
    """

    next_id = 0

    def get_container(self):
        """return bottom level container holding this object"""

    def get_root_container(self):
        """retun top level container"""

    def __init__(self):
        self.agent_id = Agent.next_id
        Agent.next_id += 1

    def get_name(self):
        """name is the agent type + the agent id"""
        return f"Agent {self.agent_id}"
