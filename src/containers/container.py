"""
Base class for all containers
"""

from src.containers.abstract_container import AbstractContainer


class Container(AbstractContainer):
    """Base class for all containers"""

    next_id = 0

    def __init__(self, *args, **kwargs):
        """Constructor"""
        self.container_id = Container.next_id
        Container.next_id += 1
        self.agents = []
        self.containers = []
        self.args = args
        self.name = ""
        for key, value in kwargs.items():
            if key == "name":
                self.name = value
            else:
                self.__setattr__(key, value)

    def add_agent(self, agent):
        """All containers must be able to add
        agents"""
        if agent in self.agents:
            raise Exception("Agent exists in container already.")

        self.agents.append(agent)

    def remove_agent(self, agent):
        """Containers must be able to remove"""
        if len(self.agents) > 0 and agent in self.agents:
            self.agents.remove(agent)
            return agent

        raise IndexError

    def add_container(self, subcontainer):
        """Containers are able to hold sub containers."""
        self.containers.append(subcontainer)
