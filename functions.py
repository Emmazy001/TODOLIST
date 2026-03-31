
def view_tasks(zipped):
    print('your tasks for today:')
    for i, j in zipped:
        print(i, j)


def add_tasks(tasks,keys):
    y = input('Enter Task:')
    tasks.append(y)
    keys.append(len(tasks))
    zipped = (zip(keys, tasks))
    print('your tasks for today:')
    for i, j in zipped:
        print(i, j)

def remove_tasks(tasks,keys):
    y = int(input('Enter Task number:'))
    tasks.pop(y - 1)
    keys.pop()
    zipped = (zip(keys, tasks))
    print('your tasks for today:')
    for i, j in zipped:
        print(i, j)


