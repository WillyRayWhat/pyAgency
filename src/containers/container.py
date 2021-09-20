"""
Base class for all containers
"""

from .abstract_container import AbstractContainer


class Container(AbstractContainer):
    """Base class for all containers"""

    next_id = 0

    def add_agent(self, agent):
        """All containers must be able to add
        agents"""

    def __init__(self):
        """Constructor"""
        self.container_id = Container.next_id
        Container.next_id += 1

    def remove_agent(self, agent):
        """Containers must be able to remove"""
