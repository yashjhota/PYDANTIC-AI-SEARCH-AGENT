import pytest
import os
from agent_utils import get_search_results # Import the function to test

# Check if the API key is available (useful for debugging, especially locally)
# The actual test execution in CI relies on the key being injected via env var
API_KEY_AVAILABLE = os.getenv("TAVILY_API_KEY") is not None

@pytest.mark.skipif(not API_KEY_AVAILABLE, reason="TAVILY_API_KEY environment variable not set")
def test_get_search_results_runs_and_returns_string():
    """
    Tests if get_search_results runs without error and returns a string
    for a simple query. Requires TAVILY_API_KEY.
    """
    query = "What is the capital of France?"
    try:
        result = get_search_results(query)
        print(f"\nAPI Result for '{query}': {result[:100]}...") # Print snippet for debugging in CI logs

        # Basic assertions: Check if we got a string result back
        assert isinstance(result, str)
        assert len(result) > 0 # Ensure the result is not empty

    except Exception as e:
        pytest.fail(f"get_search_results raised an exception: {e}")

# You could add more tests here, e.g., testing edge cases or specific expected keywords
# but this is a basic "does it run" test.
