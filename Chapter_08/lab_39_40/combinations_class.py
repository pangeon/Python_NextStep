class Combinations:

    def __init__(self, products, promototions, customers):
        self.products = products
        self.promototions = promototions
        self.customers = customers

        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

    def __next__(self):
        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1

        if self.current_promotion >= len(self.promototions):
            self.current_promotion = 0
            self.current_product += 1

        if self.current_product >= len(self.products):
            self.current_product = 0
            raise StopIteration("Stopped iteration...")
        
        item_to_return = "{} - {} - {}".format(
            self.products[self.current_product],
            self.promototions[self.current_promotion],
            self.customers[self.current_customer]
        )
        self.current_customer += 1

        return item_to_return
    
    def __iter__(self):
        return self