import typer
import csv
from faker import Faker
from src.models.bookings import Booking, BookingDates, BookingWithId
from pprint import pprint
import json
import requests
from datetime import timedelta
from src.configs import EnvConfig

BOOKINGS_CSV_FILE = "bookings.csv"
BOOKINGS_JSON_FILE = "bookings.json"

app = typer.Typer()


@app.command()
def booking_csv_gen(count: int = 1):
    with open(file=BOOKINGS_CSV_FILE, mode="w", newline="") as csv_file:
        fieldnames = Booking().model_dump().keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        faker = Faker()
        for _ in range(count):
            checkin = faker.date_between(start_date="today", end_date="+1y")
            checkout_delta = timedelta(days=faker.random_int(min=2, max=14))
            checkout = checkin + checkout_delta
            booking_dates = BookingDates(checkin=checkin.strftime("%Y-%m-%d"), checkout=checkout.strftime("%Y-%m-%d"))
            booking = Booking(
                firstname=faker.first_name(),
                lastname=faker.last_name(),
                totalprice=faker.random_int(min=50, max=150),
                depositpaid=faker.boolean(chance_of_getting_true=50),
                additionalneeds=faker.paragraphs(nb=1)[0],
                bookingdates=booking_dates,
            )
            writer.writerow(booking.model_dump())


@app.command()
def booking_csv_read():
    with open(file=BOOKINGS_CSV_FILE, mode="r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        bookings = []
        for row in reader:
            booking_dates_json_str = row["bookingdates"]
            booking_dates = json.loads(booking_dates_json_str.replace("'", '"'))
            row["bookingdates"] = booking_dates
            bookings.append(Booking.model_validate(row))
        pprint(bookings)


@app.command()
def add_bookings():
    bookings_with_id = []

    with open(file=BOOKINGS_CSV_FILE, mode="r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        url = f"{EnvConfig().url}/booking"

        for row in reader:
            booking_dates_json_str = row["bookingdates"]
            booking_dates = json.loads(booking_dates_json_str.replace("'", '"'))
            row["bookingdates"] = booking_dates
            response = requests.post(url=url, json=row)
            if response.status_code == 200:
                bookings_with_id.append(BookingWithId.model_validate(response.json()).model_dump())
                print(".", end="", flush=True)

    with open(BOOKINGS_JSON_FILE, "w") as json_file:
        json.dump(bookings_with_id, json_file, indent=4)


if __name__ == "__main__":
    app()
