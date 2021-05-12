class SequenceGenIterator:
    
    def __init__(self, min_value, step, max_value):
        self.min_value = min_value
        self.step = step
        self.max_value = max_value

        self.next_value = 0
        self.next_step = 0

    def __next__(self):
        if self.min_value > self.max_value or self.step > self.max_value:
            raise Exception('Invalid argument values')
        else:
            self.next_step = self.min_value + self.step
            self.next_value += self.next_step
            
            return self.next_value