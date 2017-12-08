correctNumber = 58
while True:
    number = int(input("Guess a number between 0 and 100: "))
    if number == correctNumber:
        print("Cool, you have found a correct number:", correctNumber)
        break
    elif number < correctNumber:
        print("The correct number is higher than", number)
    else:
        print("The correct number is less than", number)