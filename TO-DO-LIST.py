import functions
from functions import view_tasks, add_tasks, remove_tasks

tasks=[]
keys=[]
n=int(input('Enter number of tasks:'))
for i in range(n):
    x=(input('Enter task:'))
    tasks.append(x)
    keys.append(i+1)

zipped=(zip(keys,tasks))

def main():
    while True:
        print('choose option:')
        print('1.View Tasks')
        print('2.Add Tasks')
        print('3.Remove Tasks')
        print('4.Exit program')

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

main()
