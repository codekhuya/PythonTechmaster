numberOfPrimes = 500
countOfPrimes = 0
numberOfPrimesPerLine = 10
primeInLineCount = 0

i = 1

while countOfPrimes < numberOfPrimes:
    for j in range(2, i // 2):
        if i % j == 0:
            break
    else:
        countOfPrimes += 1
        print("%6d" % (i), end="")
        primeInLineCount += 1
        if primeInLineCount >= numberOfPrimesPerLine:
            print("")
            primeInLineCount = 0
    i += 1