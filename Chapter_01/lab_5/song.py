import datetime

'''
Inspired by De Mono song: https://www.youtube.com/watch?v=lmn0Qf1_eI4 
'''

song_activities = [
    'W poniedzialek, w poniedziałek ja nie mogę bo pomagam mamie', 
    'A we wtorek, a we wtorek i środę ty masz w domu pranie',
    'No a w czwartek, no a w czwartek ja mam dyżur, w piątek, w piątek dwa zebrania',
    'Ty w sobotę, ty w sobotę znów nie możesz bo na lekcje ganiasz',
    'ALE ZA TO NIEDZIELA ALE ZA TO NIEDZIELA NIEDZIELA BĘDZIE DLA NAS!!!!!!!!!'
]

def day_today():
    day_of_week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    today_weekday = datetime.datetime.today().weekday()

    return day_of_week[today_weekday]

if day_today() == 'mon':
    print(song_activities[0])
elif day_today() == 'tue' or day_today() == 'wed':
    print(song_activities[1])
elif day_today() == 'thu' or day_today() == 'fri':
    print(song_activities[2])
elif day_today() == 'sat':
    print(song_activities[3])
elif day_today() == 'sun':
    print(song_activities[4])