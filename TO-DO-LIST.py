
from functions import *

def main():
    tasks = []
    keys = []


    while True:
        try:
            n = int(input('Enter number of tasks:'))
            for i in range(n):
                x = (input('Enter task:'))
                tasks.append(x)
                keys.append(i + 1)
            break
        except ValueError:
            print('invalid input')


    zipped = (zip(keys, tasks))

    while True:
        print('choose option:')
        print('1.View Tasks')
        print('2.Add Tasks')
        print('3.Remove Tasks')
        print('4.Exit program')
        try:
            choice = int(input('Enter your choice:'))
            if choice==1:
               view_tasks(zipped)
            elif choice==2:
                add_tasks(tasks,keys)

            elif choice==3:
               remove_tasks(tasks,keys)

            elif choice==4:
                break
            else:
                print('invalid choice')
        except ValueError:
            print('invalid input')
            continue

main()
