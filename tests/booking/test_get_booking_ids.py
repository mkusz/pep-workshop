import requests
from pytest_check import check


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
