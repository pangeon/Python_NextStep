from cake.cake_class import Cake, add_extra_additives
from cake.special_cake_class import SpecialCake
from cake.promo_class import Promo
from cake.promo_cake_class import PromoCake

from datetime import date
from datetime import timedelta  

def lab_30_31_32():
    cake01 = Cake(
        'Vanilla Cake','cake', 
        'vanilla', 
        [], 
        'cream'
    )
    print(cake01)
    
    cake01.add_additives(
        [
            'strawberries', 
            'sugar-flowers'
        ]
    )
    add_extra_additives(
        cake01,
        [
            'strawberries', 
            'sugar-flowers',
            'chocolade', 
            'nuts'
        ]
    )
    cake01 += ['cherry', 'cream']
    cake01 += 'bakery powder'
    cake01.show_info()

    birthday = SpecialCake(
        'Vanilla Cake',
        'cake', 
        'vanilla', 
        [
            'chocolade', 
            'nuts'
        ], 
        'cream',
        
        'birthday', 
        'standard', 
        'hearts', 
        '15'
    )
    wedding  = SpecialCake(
        'Vanilla Cake',
        'cake', 
        'vanilla', 
        [
            'whipped cream', 
            'coconut shirms'
        ], 
        'strawberries cream',

        'wedding', 
        'pyramid', 
        'pigeons', 
        'Patricia & Tom'
    )
 
    birthday.show_info()
    wedding.show_info()

    for cake in SpecialCake.bakery_offer:
        print(cake.full_name)
        cake.show_info()
    
def lab_33():
    cake = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
    cake.show_info()
    
    promo10 = Promo("DISCOUNT - no additional conditions", 0.15, date.today(), date.today() + timedelta(days=14),0)
    print(promo10.full_name)

    promo_cake = PromoCake(cake, promo10)
    promo_cake.show_info()
    print(promo_cake.full_name)
    print(PromoCake.__mro__)

if __name__ == "__main__":
    lab_30_31_32()
    lab_33()


    
