import random

# use Operating System random generator engine
print('System random:', random.SystemRandom())

print('Random:', random.random())

# random from 1 to 100
print('Random Integer:', random.randint(1, 100))

#start - stop - step
print('Random range:', random.randrange(0, 20, 2))

#http://mathworld.wolfram.com/UniformDistribution.html
print('Random uniform:', random.uniform(8, 20)) # phan phoi theo xac xuat

#http://mathworld.wolfram.com/TriangularDistribution.html
print('Random triangular:', random.triangular(0, 10, 1))
print('Random triangular:', random.triangular(0, 10, 0))


print('Random choie:',random.choice([1, 3, 5, 2, 6, 10, -10, -3, 9]))

items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items) # Xao tron phan tu
print('Xao tron phan tu:', items)

print('Random choice:', random.choice('abcdefghij')) #randome from
print('Random sample:', random.sample([1, 2, 3, 4, 5], 3)) # Three samples without replacement
#A common task is to make a random.choice() with weighted probabilities.
#If the weights are small integer ratios, a simple technique is to build a sample population with repeats:

weighted_choices = [('Red', 3), ('Blue', 2), ('Yellow', 1),('Green', 4)]
population = [val for val, cnt in weighted_choices for i in range(cnt)]
print(population)
print(random.choice(population))