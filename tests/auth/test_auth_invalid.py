import requests
from pytest_check import check

WRONG_PASSWORD = "wrong_password"


def test_wrong_password(auth_url, user_config):
    json: dict[str, str] = {"username": user_config.username, "password": WRONG_PASSWORD}
    response: requests.Response = requests.post(url=auth_url, json=json)

    with check:
        assert "reason" in response.json()

    with check:
        assert response.status_code == 200


def test_wrong_password_model(auth_url, user_config):
    json = user_config.model_dump()
    json["password"] = WRONG_PASSWORD
    response: requests.Response = requests.post(url=auth_url, json=json)

    with check:
        assert "reason" in response.json()

    with check:
        assert response.status_code == 200


def test_wrong_no_password_exclude(auth_url, user_config):
    json = user_config.model_dump(exclude={"password"})
    response: requests.Response = requests.post(url=auth_url, json=json)

    with check:
        assert "reason" in response.json()

    with check:
        assert response.status_code == 200


def test_wrong_no_password_include(auth_url, user_config):
    json = user_config.model_dump(include={"username"})
    response: requests.Response = requests.post(url=auth_url, json=json)

    with check:
        assert "reason" in response.json()

    with check:
        assert response.status_code == 200
