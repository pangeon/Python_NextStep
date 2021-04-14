cake_01 = {
    'taste': 'vanilia',
    'glaze': 'chocolade',
    'text': 'Happy Brithday',
    'weight': 0.7,
}

cake_02 = {
    'taste': 'tee',
    'glaze': 'lemon',
    'text': 'Happy Python Coding',
    'weight': 1.3,
}
        
def show_cake_info(taste, glaze, text, weight):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        taste, glaze, text, weight))
    
def show_cake_info_obj(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake['taste'], cake['glaze'], cake['text'], cake['weight']))
    
show_cake_info(
    cake_01['taste'], 
    cake_01['glaze'], 
    cake_01['text'], 
    cake_01['weight']
)

show_cake_info(
    cake_02['taste'], 
    cake_02['glaze'], 
    cake_02['text'], 
    cake_02['weight']
)
cakes = [cake_01, cake_02]

for cake in cakes:
    show_cake_info_obj(cake)
