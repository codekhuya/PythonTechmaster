'''
tasks = ['Get requirements', 'Design', 'Code', 'Test', 'Ship', 'Fix bug']
for task in tasks:
    print(task)
for i in range(len(tasks)):
    print("task %d %s" % (i, tasks[i]))


name = 'Jame Cook'
for phantu in name:
    print(phantu)

for char in reversed(name):
    print(char)

numbers = [12, 16, 17, 24, 29, 30]
for i in numbers:
    if i % 2 == 1: #check if odd number
        continue
    print(i)
print('done')
'''

#PRIME NUMBER
for num in range(1, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print("%d equals %d * %d" % (num, i, j))
            break #Thoat khoi vong lap trong cung
    else:
        print(num, "is prime number.")

