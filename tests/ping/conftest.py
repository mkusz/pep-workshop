import pytest


@pytest.fixture(scope="session")
def ping_url(env_config) -> str:
    return f"{env_config.url}/ping"
