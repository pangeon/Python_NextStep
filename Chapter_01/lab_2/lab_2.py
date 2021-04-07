days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days.copy() 

workdays.remove('sat')
workdays.remove('sun')

print(days, id(days))
print(workdays, id(workdays))



