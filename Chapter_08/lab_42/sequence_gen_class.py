from sequence_gen_iterator import SequenceGenIterator
from exceptions.sequnence_invalid_argument_exception_class import SequenceInvalidArgumentException 

class SequenceGen:

    def __init__(self, min_value, step, max_value):
        
        self.min_value = min_value
        self.step = step
        self.max_value = max_value 
        
        if self.min_value > self.max_value or self.step > self.max_value:
            raise SequenceInvalidArgumentException("Error during create sequence")

        self.next_value = 0
        self.next_step = 0

        self.iterator = SequenceGenIterator(self.min_value, self.step, self.max_value)
    
    def __iter__(self):
        return self.iterator