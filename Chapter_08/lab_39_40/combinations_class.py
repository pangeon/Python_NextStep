class Combinations:

    def __init__(self, products, promototions, customers):
        self.products = products
        self.promototions = promototions
        self.customers = customers
    
    def __iter__(self):
        return self
    
    def __getitem__(self, item):
        all_combinations = len(self.products) * len(self.promototions) * len(self.customers)
        if  all_combinations < item:
            raise StopIteration("Iteration had stopped...")
        else:
            position_products = item // (len(self.promototions) * len(self.customers))
            item = item % (len(self.promototions) * len(self.customers))
            
            position_promotions = item // len(self.customers)
            item = item % len(self.customers)

            position_cutomers = item

        return "{} - {} - {}".format(
            self.products[position_products],
            self.promototions[position_promotions],
            self.customers[position_cutomers]
        ) 
