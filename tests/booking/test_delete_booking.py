import requests
from pytest_check import check
import pytest


@pytest.mark.wip
def test_delete_booking_by_id(booking_url, single_booking_with_id, token):
    headers = {"Cookie": f"token={token}"}

    response: requests.Response = requests.delete(
        url=f"{booking_url}/{single_booking_with_id.bookingid}", headers=headers
    )
    with check:
        assert response.status_code == 201

    response: requests.Response = requests.get(url=f"{booking_url}/{single_booking_with_id.bookingid}")

    with check:
        assert response.status_code == 404
