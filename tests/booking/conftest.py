import pytest
import json
from src.models.bookings import BookingWithId, Booking
from app import BOOKINGS_JSON_FILE
import random
import requests


@pytest.fixture(scope="session")
def booking_url(env_config) -> str:
    return f"{env_config.url}/booking"


@pytest.fixture(scope="session")
def all_bookings_with_id_from_json() -> list[BookingWithId]:
    bookings_with_id = []

    with open(BOOKINGS_JSON_FILE, "r") as json_file:
        bookings_from_json = json.load(json_file)
        for booking in bookings_from_json:
            bookings_with_id.append(BookingWithId.model_validate(booking))

    return bookings_with_id


@pytest.fixture(scope="function")
def single_booking_with_id_from_json(all_bookings_with_id_from_json) -> BookingWithId:
    return all_bookings_with_id_from_json[random.randrange(0, len(all_bookings_with_id_from_json) - 1)]


@pytest.fixture(scope="session")
def all_bookings_with_id(booking_url) -> list[int]:
    response: requests.Response = requests.get(url=booking_url)
    booking_ids = []
    if response.status_code == 200:
        booking_ids = [booking["bookingid"] for booking in response.json()]

    return booking_ids


@pytest.fixture(scope="function")
def single_booking_with_id(booking_url, all_bookings_with_id) -> BookingWithId:
    booking_id = all_bookings_with_id[random.randrange(0, len(all_bookings_with_id) - 1)]
    response: requests.Response = requests.get(url=f"{booking_url}/{booking_id}")

    booking = Booking.model_validate(response.json())
    booking_with_id = BookingWithId(
        bookingid=booking_id,
        booking=booking,
    )
    return booking_with_id
