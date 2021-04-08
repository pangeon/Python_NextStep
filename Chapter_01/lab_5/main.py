import datetime

## example 1

price = 123
bonus = 23
bonus_granted = True
     
# if bonus_granted:
#     price -= bonus
    
# print(price)

price -= bonus if bonus_granted else price
print(price)

## example 2

rating = 5
    
# if rating == 5:
#     print('very good')
# elif rating == 4:
#     print('good')
# else:
#     print('weak')

print('very good') if rating == 5 else print('weak') if rating == 4 else print('good')