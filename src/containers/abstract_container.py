"""
abstract base class for all containers
"""

from abc import ABCMeta, abstractmethod


class AbstractContainer(metaclass=ABCMeta):
    """
    Abstract container is a base class for all container objects
    """

    @abstractmethod
    def add_agent(self, agent):
        """Add an agent"""

    def remove_agent(self, agent):
        """remove an agent"""
