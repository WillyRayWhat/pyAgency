"""
test class for all contianers
"""
import pytest

from src.agents.agent import Agent
from src.containers.container import Container


# containers should have auto-incrementing ids
def test_container_id():
    """Test the auto-incrememting id"""
    container = Container()
    assert container.container_id == 0
    container = Container()
    container = Container()
    assert container.container_id == 2


def test_container_add():
    """Test that we can add agents to containers"""
    container = Container()
    agent = Agent()
    container.add_agent(agent)
    assert len(container.agents) == 1


def test_container_unique():
    """test that container refuses duplicate agents"""
    container = Container()
    agent = Agent()
    container.add_agent(agent)
    with pytest.raises(Exception):
        container.add_agent(agent)


def test_container_remove():
    """containers should be able to have an agent removed"""
    cont = Container()
    agent = Agent()
    cont.add_agent(agent)
    rem = cont.remove_agent(agent)
    assert rem is agent
    assert len(cont.agents) == 0
    with pytest.raises(IndexError):
        cont.remove_agent(agent)


def test_container_name():
    """containers should be able to get a name"""
    container = Container(name="main")
    assert container.name == "main"


def test_container_nesting():
    """Containers can be nested"""
    container = Container(name="main")
    sub0 = Container(name="sub0")
    sub1 = Container(name="sub1")
    container.add_container(sub0)
    container.add_container(sub1)
    assert len(container.containers) == 2
