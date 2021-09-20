"""
test class for all contianers
"""
from src.containers.container import Container


# containers should have auto-incrementing ids
def test_container_id():
    """Test the auto-incrememting id"""
    container = Container()
    assert container.container_id == 0
    container = Container()
    container = Container()
    assert container.container_id == 2
