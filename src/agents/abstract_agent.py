"""
Abstract class to represent the interface for all agents

"""

from abc import ABCMeta, abstractmethod


class AbstractAgent(metaclass=ABCMeta):
    """Abstract base classfor all agents"""

    @abstractmethod
    def get_container(self):  # pragma: no cover
        """Return the container that holds this agent"""

    @abstractmethod
    def get_root_container(self):  # pragma: no cover
        """return the top-level container thata holds this gent"""
