import pydantic


class BookingDates(pydantic.BaseModel):
    checkin: str = ""
    checkout: str = ""


class Booking(pydantic.BaseModel):
    firstname: str = ""
    lastname: str = ""
    totalprice: int = 0
    depositpaid: bool = False
    additionalneeds: str = ""
    bookingdates: BookingDates = BookingDates()


class BookingWithId(pydantic.BaseModel):
    bookingid: int | None = None
    booking: Booking | None = None
