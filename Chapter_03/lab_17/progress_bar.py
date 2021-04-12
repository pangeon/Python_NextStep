import time

def show_progress(repetitions = 100, char_to_repeat = "*"):
    print('{:<100}'.format(char_to_repeat * repetitions), '{:>50}'.format(repetitions), "%")

for i in range(1, 101):
    time.sleep(i / 100)
    show_progress(i, '#')


