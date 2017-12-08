'''
print("Hello Py")
print('Hello Pyman')
name = "Thanh"
age = 28
print("My nam is", name, ". I am ", age)
print('My name is %s. I am %d' % (name, age))

primeNum = [1, 2, 3, 5, 7, 11, 13, 17, 19]
i = 0
for prime in primeNum:
    print('%2d: %2d' % (i, prime))
    i += 1

for prime in primeNum:
    print("%2d, " % prime, end='')

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

#Khong can thu tu tham so
print('We are the {} who say "{}!"'.format('knight', "Ni"))

#Co thu tu tham so
print ("{1} and {0}".format('spam', 'eggs'))

#Keyword
print('This {food} is {adjective}.'.format(food = 'spam', adjective='absolutely horrible'))

#Ket hop so thu tu va keyword
print('The story of {0}, {1} and {other}.'.format('Bill', 'Manfred', other='Georg'))
'''

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name,phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
    