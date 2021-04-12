from datetime import datetime


"""
- f_minutes - obliczającą różnicę między datami i wyrażającą ją w minutach
- f_hours - obliczającą różnicę między datami i wyrażającą ją w godzinach
- f_days - obliczającą różnicę między datami i wyrażającą ją w dniach
"""


start = datetime(1986, 2, 15, 16, 30, 00)
end = datetime.now()

duration = end - start
duration_in_s = duration.total_seconds()


def time_span_m(start, end):
    return divmod(duration_in_s, 60)[0]


def time_span_h(start, end):
    return divmod(duration_in_s, 3600)[0]
 

def time_span_d(start, end):
    return divmod(duration_in_s, 86400)[0]


print("Since your birthday passed:")
print(time_span_m(start, end), "minutes")
print(time_span_h(start, end), "hours")
print(time_span_d(start, end), "day")


def create_function(span):
    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 3600
    elif span == 'd':
        sec = 86400
    else:
        sec = -1

    source = '''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
'''.format(sec)
    exec(source, globals())

    return f # ! This is not error, look above -> exec(source, globals()) 

f_minutes = create_function('m')
f_hours = create_function('h')
f_days = create_function('d')

print("\n" + "*"*40 + "\n")

print("Since your birthday passed:")
print(int(f_minutes(start, end)), "minutes")
print(int(f_hours(start, end)), "hours")
print(int(f_days(start, end)), "days")







