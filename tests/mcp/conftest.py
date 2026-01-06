
import pytest
from unittest.mock import MagicMock, AsyncMock

@pytest.fixture
def mock_db_manager():
    """Mock DatabaseManager."""
    mock = MagicMock()
    mock.get_connection = MagicMock()
    return mock

@pytest.fixture
def mock_neo4j_manager():
    """Mock Neo4jManager."""
    mock = MagicMock()
    # verify_connectivity is often awaited or check
    mock.verify_connectivity = AsyncMock(return_value=True)
    return mock

@pytest.fixture
def mock_auth_handler():
    """Mock AuthHandler."""
    mock = MagicMock()
    mock.verify_token = AsyncMock(return_value={"user_id": "test_user"})
    return mock

@pytest.fixture
def mock_mcp_context():
    """Mock MCP Context for tools."""
    mock = MagicMock()
    # Add any specific MCP context methods here if needed
    return mock
