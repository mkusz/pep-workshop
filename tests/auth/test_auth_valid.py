from http import HTTPStatus

import requests
from pytest_check import check


def test_valid(auth_url, user_config):
    response: requests.Response = requests.post(url=auth_url, json=user_config.model_dump())

    with check:
        assert "token" in response.json()

    with check:
        assert response.status_code == HTTPStatus.OK


def test_valid_with_extra_field(auth_url, user_config):
    json = user_config.model_dump()
    json["extra"] = "some_value"
    response: requests.Response = requests.post(url=auth_url, json=json)

    with check:
        assert "token" in response.json()

    with check:
        assert response.status_code == HTTPStatus.OK
