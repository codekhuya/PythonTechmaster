canFly = True
canSwim = False
canChaseMouse = True

if canFly:
    if canSwim:
        print('I am Duck')
    elif canChaseMouse:
        print('I am Eagle')
    else:
        print('I am Bird')
else:
    print('I am Chicken')

for i in range(0, 10):
    if i % 2 == 0:
        print(i)

workday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
holiday = ['30/04', '01/05', '02/09']

day = "Sunday"
date = "02/05"

if day in weekend or date in holiday:
    print("Let's have fun! :D")
else:
    print("Go to work")