from exceptions.trip_exception_class import TripException
from exceptions.trip_name_exception_class import TripNameException
from exceptions.trip_date_exception_class import TripDateException

class Trip:

    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
    
    def check_data(self):
        if len(self.title) == 0:
            raise TripNameException("Name error !")
        if self.start > self.end:
            raise TripDateException("Date error !")
    
    @classmethod
    def publish_offer(cls, trips):
        list_of_errors = []
        for trip in trips:
            try:
                trip.check_data()
            except TripNameException as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except TripDateException as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))

        if list_of_errors != []:
            raise TripException("The list of trips has errors", list_of_errors)
        else:
            print("the offer will be published...")