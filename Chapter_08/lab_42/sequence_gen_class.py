from sequence_gen_iterator import SequenceGenIterator 

class SequenceGen:

    def __init__(self, min_value, step, max_value):
        self.min_value = min_value
        self.step = step
        self.max_value = max_value

        self.next_value = 0
        self.next_step = 0

        self.iterator = SequenceGenIterator(self.min_value, self.step, self.max_value)
    
    def __iter__(self):
        return self.iterator