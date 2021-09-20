"""
abstract base class for all containers
"""

from abc import ABCMeta, abstractmethod


class AbstractContainer(metaclass=ABCMeta):
    """
    Abstract container is a base class for all container objects
    """

    @abstractmethod
    def add_agent(self, agent):  # pragma: no cover
        """Add an agent"""

    def remove_agent(self, agent):  # pragma: no cover
        """remove an agent"""
