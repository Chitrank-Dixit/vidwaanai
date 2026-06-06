import pytest
from unittest.mock import MagicMock, patch
from src.llm.openai_client import OpenAIClient


@pytest.fixture
def mock_openai_response():
    mock_response = MagicMock()
    mock_choice = MagicMock()
    mock_message = MagicMock()
    mock_message.content = "Mocked OpenAI response"
    mock_choice.message = mock_message
    mock_response.choices = [mock_choice]
    return mock_response


@patch("src.llm.openai_client.OpenAI")
def test_openai_client_initialization(mock_openai):
    client = OpenAIClient(api_key="test-key", model="gpt-4-test")
    assert client.model == "gpt-4-test"
    mock_openai.assert_called_once_with(api_key="test-key")


@patch("src.llm.openai_client.OpenAI")
def test_openai_client_generate_success(mock_openai, mock_openai_response):
    # Setup mock
    mock_instance = MagicMock()
    mock_openai.return_value = mock_instance
    mock_instance.chat.completions.create.return_value = mock_openai_response

    # Initialize client
    client = OpenAIClient(api_key="test-key")

    # Generate
    prompt = "What is the capital of France?"
    response = client.generate(prompt=prompt, max_tokens=100, temperature=0.5)

    assert response == "Mocked OpenAI response"
    mock_instance.chat.completions.create.assert_called_once_with(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a knowledgeable assistant about Indian scriptures.",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=100,
        temperature=0.5,
    )


@patch("src.llm.openai_client.OpenAI")
def test_openai_client_generate_empty_response(mock_openai):
    # Setup mock with empty response
    mock_response = MagicMock()
    mock_choice = MagicMock()
    mock_message = MagicMock()
    mock_message.content = ""
    mock_choice.message = mock_message
    mock_response.choices = [mock_choice]

    mock_instance = MagicMock()
    mock_openai.return_value = mock_instance
    mock_instance.chat.completions.create.return_value = mock_response

    # Initialize client
    client = OpenAIClient(api_key="test-key")

    # Generate
    response = client.generate(prompt="Test empty")
    assert response == ""


@patch("src.llm.openai_client.OpenAI")
def test_openai_client_generate_exception(mock_openai):
    # Setup mock to raise exception
    mock_instance = MagicMock()
    mock_openai.return_value = mock_instance
    mock_instance.chat.completions.create.side_effect = Exception("API Error")

    # Initialize client
    client = OpenAIClient(api_key="test-key")

    # Generate and expect exception
    with pytest.raises(Exception, match="API Error"):
        client.generate(prompt="Test exception")
