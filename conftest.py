import pytest


@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {
            "width": 1520,
            "height": 780,
        }
    }