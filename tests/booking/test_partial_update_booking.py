import requests
from pytest_check import check
from src.models.bookings import Booking
import pytest
from faker import Faker


@pytest.mark.wip
def test_update_names(booking_url, single_booking_with_id, token):
    headers = {"Cookie": f"token={token}"}

    faker = Faker()
    first_name = faker.first_name()
    last_name = faker.last_name()

    expected_booking: Booking = single_booking_with_id.booking
    expected_booking.firstname = first_name
    expected_booking.lastname = last_name

    response: requests.Response = requests.patch(
        url=f"{booking_url}/{single_booking_with_id.bookingid}",
        headers=headers,
        json={"firstname": first_name, "lastname": last_name},
    )
    with check:
        assert response.status_code == 200

    observed_booking: Booking = Booking.model_validate(response.json())
    print(f"\n{expected_booking}\n{observed_booking}")

    with check:
        assert observed_booking == expected_booking

    response: requests.Response = requests.get(url=f"{booking_url}/{single_booking_with_id.bookingid}")

    with check:
        assert response.status_code == 200

    observed_booking: Booking = Booking.model_validate(response.json())
    print(f"\n{expected_booking}\n{observed_booking}")

    with check:
        assert observed_booking == expected_booking
