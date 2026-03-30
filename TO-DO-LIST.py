
Tasks=[]
keys=[]
n=int(input('Enter number of tasks:'))
for i in range(n):
    x=(input('Enter task:'))
    Tasks.append(x)
    keys.append(i+1)

zipped=(zip(keys,Tasks))


print('choose option:')
print('1.View Tasks')
print('2.Add Tasks')
print('3.Remove Tasks')
#print('4.Exit program')

choice=int(input('Enter your choice:'))
if choice==1:
    print('your tasks for today:')
    for i, j in zipped:
        print(i, j)

if choice==2:
    y=input('Enter Task:')
    Tasks.append(y)
    keys.append(len(Tasks))
    zipped=(zip(keys,Tasks))
    print('your tasks for today:')
    for i, j in zipped:
        print(i, j)

if choice==3:
    y=int(input('Enter Task number:'))
    Tasks.pop(y-1)
    keys.pop()
    zipped = (zip(keys, Tasks))
    print('your tasks for today:')
    for i, j in zipped:
        print(i, j)


