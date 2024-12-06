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


# def test_get_booking_by_first_name(booking_url, single_booking_with_id):
#     params = {
#         "firstname": single_booking_with_id.booking.firstname.lower(),
#         "lastname": single_booking_with_id.booking.lastname.lower(),
#     }
#     print(params)
#     response: requests.Response = requests.get(url=booking_url, params=params)
#     print(response.json())


def test_get_booking_by_id(booking_url, single_booking_with_id):
    response: requests.Response = requests.get(url=f"{booking_url}/{single_booking_with_id.bookingid}")
    print(single_booking_with_id)
    print(response.json())
