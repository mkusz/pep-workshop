import pytest
import requests

from src.configs import EnvConfig
from src.configs import UserConfig


@pytest.fixture(scope="session")
def env_config() -> EnvConfig:
    """Environment variables (like url)"""
    # yield EnvConfig()
    # print("End")
    return EnvConfig()


@pytest.fixture(scope="session")
def user_config() -> UserConfig:
    """Username and password for authentication"""
    return UserConfig()


@pytest.fixture(scope="module")
def token(env_config, user_config) -> str | None:
    response: requests.Response = requests.post(url=f"{env_config.url}/auth", json=user_config.model_dump())

    # return response.json()["token"] if response.status_code == 200 and "token" in response.json() else None

    if response.status_code != 200:
        return None

    if "token" not in response.json():
        return None

    return response.json()["token"]
