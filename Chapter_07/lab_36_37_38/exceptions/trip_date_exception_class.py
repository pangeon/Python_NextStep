from exceptions.trip_exception_class import TripException

class TripDateException(TripException):

    def __init__(self, text):
        super().__init__(
            text, 
            "Name of the trip is missing. You need to name the trip somehow..."
        )