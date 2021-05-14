class SequenceException(Exception):

    def __init__(self, text, description):
        super().__init__(text)
        self.description = description
    
    def __str__(self):
        return "{}, info: {}".format(
            super().__str__(), self.description
        )