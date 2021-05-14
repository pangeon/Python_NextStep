from exceptions.sequence_exception_class import SequenceException

class SequenceInvalidArgumentException(SequenceException):

    def __init__(self, text):
        super().__init__(
            text, 
            "Incorrect init sequence params: min > max and step > max"
        )
