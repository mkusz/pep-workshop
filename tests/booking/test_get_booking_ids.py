import requests
from pytest_check import check
from src.models.bookings import Booking
import pytest


@pytest.mark.smoke
def test_get_all_booking_ids(booking_url):
    response: requests.Response = requests.get(url=booking_url)

    with check:
        assert response.status_code == 200

    with check:
        assert len(response.json()) > 0

    with check:
        assert "bookingid" in response.json()[0]

    with check:
        assert isinstance(response.json()[0]["bookingid"], int)


@pytest.mark.wip
@pytest.mark.xfail
def test_get_booking_by_first_name(booking_url, single_booking_with_id):
    params = {
        "firstname": single_booking_with_id.booking.firstname.lower(),
        "lastname": single_booking_with_id.booking.lastname.lower(),
    }
    print(params)
    response: requests.Response = requests.get(url=booking_url, params=params)
    assert len(response.json()) > 0
