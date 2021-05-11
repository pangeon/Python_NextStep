class Trip:

    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
    
    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")
    
    @classmethod
    def publish_offer(cls, trips):
        list_of_errors = []
        for trip in trips:
            try:
                trip.check_data()
            except ValueError as e:
                info_error = "{} - {}".format(trip.symbol, e)
                list_of_errors.append(info_error)
            except Exception as e:
                info_error = "{} - {}".format(trip.symbol, e)
                list_of_errors.append(info_error)

        if list_of_errors != []:
            raise Exception("The list of trips has errors {}".format(list_of_errors))
            print(list_of_errors)
        else:
            print("the offer will be published...")