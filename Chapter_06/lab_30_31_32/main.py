from cake.cake_class import Cake, add_extra_additives
from cake.special_cake_class import SpecialCake

if __name__ == "__main__":
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
    

    
