class Promo:
 
    def __init__(
        self, 
        name, 
        discount, 
        start_date, 
        end_date, 
        minimal_order
    ):
        self.name = name
        self.discount = discount
        self.start_date = start_date
        self.end_date =  end_date
        self.minimal_order = minimal_order

    @property
    def full_name(self):
        return "PROMO {0:s} {1:.0%}".format(self.name, self.discount)
    