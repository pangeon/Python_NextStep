class NoDuplicates:

    '''
        Cake class wrapper 
    '''

    def __init__(self, funct):
        self.funct = funct


    def __call__(self, cake, additives):
        no_duplicate_list = []
        for a in additives:
            if not a in cake.additives:
                no_duplicate_list.append(a)
        self.funct(cake, no_duplicate_list)