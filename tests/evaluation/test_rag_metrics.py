
import pytest
import json
import os
import time
from deepeval.metrics import FaithfulnessMetric, AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from deepeval import assert_test
from src.core.agent_service import AgentService

# Load Golden Dataset
DATASET_PATH = os.path.join(os.path.dirname(__file__), "golden_dataset.json")
try:
    with open(DATASET_PATH, "r") as f:
        GOLDEN_DATASET = json.load(f)
except FileNotFoundError:
    GOLDEN_DATASET = []

@pytest.fixture(scope="module")
def agent_service():
    """
    Initialize AgentService.
    Ensures that we are running inside the container where env vars and network are available.
    """
    # Simply instantiating AgentService should work if env vars are correct
    return AgentService()

@pytest.mark.parametrize("case", GOLDEN_DATASET)
def test_rag_quality(agent_service, case):
    """
    Test RAG pipeline quality using DeepEval metrics.
    """
    input_text = case["input"]
    expected_output = case["expected_output"]
    
    print(f"\n--- Testing Query: {input_text} ---")
    
    # 1. Run Pipeline
    start = time.time()
    response = agent_service.process_query(input_text, session_id="eval_session")
    duration = time.time() - start
    
    actual_output = response["answer"]
    retrieval_context = response.get("retrieval_context", [])
    
    print(f"Time: {duration:.2f}s")
    print(f"Context Ids: {len(retrieval_context)}")
    
    # 2. Define DeepEval Test Case
    test_case = LLMTestCase(
        input=input_text,
        actual_output=actual_output,
        expected_output=expected_output,
        retrieval_context=retrieval_context
    )
    
    # 3. Define Metrics
    # Faithfulness: Is answer derived from context? (Hallucination check)
    faithfulness = FaithfulnessMetric(threshold=0.5, include_reason=True)
    
    # Relevancy: Is answer relevant to the input?
    relevancy = AnswerRelevancyMetric(threshold=0.5, include_reason=True)
    
    # Note: Metrics require OpenAI API Key in env (OPENAI_API_KEY)
    # If key is missing, these will fail or warn.
    # Use assert_test to automatically run and log to DeepEval platform (if configured)
    # or just use metric.measure() locally.
    
    # We use measure() and assert manually to avoid requiring 'deepeval login'
    faithfulness.measure(test_case)
    relevancy.measure(test_case)
    
    print(f"Faithfulness: {faithfulness.score} (Reason: {faithfulness.reason})")
    print(f"Relevancy: {relevancy.score} (Reason: {relevancy.reason})")
    
    assert faithfulness.is_successful(), f"Faithfulness Failed: {faithfulness.reason}"
    assert relevancy.is_successful(), f"Relevancy Failed: {relevancy.reason}"
