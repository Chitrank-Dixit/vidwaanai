from unittest.mock import MagicMock, patch

import pytest
import requests

from src.llm.lmstudio_client import LMStudioClient


def test_lmstudio_client_initialization():
    client = LMStudioClient(
        base_url="http://test:1234/v1/", model_name="test-model", timeout=60
    )
    assert client.base_url == "http://test:1234"
    assert client.model_name == "test-model"
    assert client.timeout == 60


@patch("src.llm.lmstudio_client.requests.post")
def test_lmstudio_client_generate_success(mock_post):
    # Setup mock response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "choices": [{"message": {"content": "Mocked LM Studio response"}}]
    }
    mock_post.return_value = mock_response

    # Initialize client
    client = LMStudioClient(base_url="http://localhost:1234", model_name="test-model")

    # Generate
    response = client.generate(prompt="Hello", max_tokens=128, temperature=0.8)

    assert response == "Mocked LM Studio response"
    mock_post.assert_called_once_with(
        "http://localhost:1234/v1/chat/completions",
        json={
            "model": "test-model",
            "messages": [{"role": "user", "content": "Hello"}],
            "max_tokens": 128,
            "temperature": 0.8,
            "stream": False,
        },
        timeout=120,
    )


@patch("src.llm.lmstudio_client.requests.post")
def test_lmstudio_client_generate_unexpected_format(mock_post):
    mock_response = MagicMock()
    mock_response.json.return_value = {"unexpected": "format"}
    mock_post.return_value = mock_response

    client = LMStudioClient()
    response = client.generate(prompt="Hello")
    assert response == ""


@patch("src.llm.lmstudio_client.requests.post")
def test_lmstudio_client_generate_timeout(mock_post):
    mock_post.side_effect = requests.exceptions.Timeout("Timeout")

    client = LMStudioClient()
    with pytest.raises(requests.exceptions.Timeout):
        client.generate(prompt="Hello")


@patch("src.llm.lmstudio_client.requests.post")
def test_lmstudio_client_generate_connection_error(mock_post):
    mock_post.side_effect = requests.exceptions.ConnectionError("Connection Error")

    client = LMStudioClient()
    with pytest.raises(requests.exceptions.ConnectionError):
        client.generate(prompt="Hello")


@patch("src.llm.lmstudio_client.requests.get")
def test_lmstudio_client_check_connection_success(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {"data": [{"id": "model-1"}]}
    mock_get.return_value = mock_response

    client = LMStudioClient(base_url="http://localhost:1234")
    result = client.check_connection()

    assert result is True
    mock_get.assert_called_once_with("http://localhost:1234/v1/models", timeout=5)


@patch("src.llm.lmstudio_client.requests.get")
def test_lmstudio_client_check_connection_failure(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError("Connection Error")

    client = LMStudioClient()
    result = client.check_connection()

    assert result is False
