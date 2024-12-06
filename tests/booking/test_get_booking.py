import requests
from pytest_check import check
from src.models.bookings import Booking
import pytest


@pytest.mark.wip
def test_get_booking_by_id(booking_url, single_booking_with_id):
    response: requests.Response = requests.get(url=f"{booking_url}/{single_booking_with_id.bookingid}")

    with check:
        assert response.status_code == 200

    response_json = response.json()

    expected_booking: Booking = single_booking_with_id.booking
    observed_booking: Booking = Booking.model_validate(response_json)
    print(f"\n{expected_booking}\n{observed_booking}")

    with check:
        assert observed_booking == expected_booking

    with check:
        assert set(response_json.keys()) == set(expected_booking.model_dump().keys())
