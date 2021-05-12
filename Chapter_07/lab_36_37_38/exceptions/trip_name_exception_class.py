from exceptions.trip_exception_class import TripException

class TripNameException(TripException):

    def __init__(self, text):
        super().__init__(
            text,
            "The dates are incorrect. The starting date should be earlier than the ending date..."
        )