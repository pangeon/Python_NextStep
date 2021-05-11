from cake.cake_class import Cake
from cake.promo_class import Promo


class PromoCake(Cake, Promo):
    
    def __init__(self, cake, promo):
        Cake.__init__(self, cake.name, cake.kind, cake.taste, cake.additives,cake.filling)
        Promo.__init__(self, promo.name, promo.discount, promo.start_date, promo.end_date, promo.minimal_order)
    
    # @property
    # def full_name(self):
    #     return str.format("{}{}", Cake.__class__, Promo.__class__)


