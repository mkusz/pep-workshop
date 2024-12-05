import pytest


@pytest.fixture(scope="session")
def booking_url(env_config) -> str:
    return f"{env_config.url}/booking"
