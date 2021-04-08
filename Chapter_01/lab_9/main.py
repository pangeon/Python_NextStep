projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for project, leader in zip(projects, leaders):
    print('The leader of "{}" is {}'.format(project, leader))

print("\n" + "*"*20 + "\n")
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for project, leader, date in zip(projects, leaders, dates):
    print('The leader of "{}" is {} \non date: {}'.format(project, leader, date))

print("\n" + "*"*20 + "\n")

for index, (project, leader, date) in enumerate(zip(projects, leaders, dates)):
    print('{} - The leader of "{}" is {} on date: {}'.format(index+1, project, leader, date))




