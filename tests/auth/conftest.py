import pytest


@pytest.fixture(scope="session")
def auth_url(env_config) -> str:
    return f"{env_config.url}/auth"
