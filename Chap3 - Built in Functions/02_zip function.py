x = [1, 2, 3]
y = [4 ,5, 6, 7]
zipped = zip(x, y)
print(list(zipped))

days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
fruits = ['Orange', "Apple", "Peach"]
drinks = ['Coffee', 'Tea', ' Beer']
desserts = ['Tiramisu', 'Ice Cream', 'Pie', 'Pudding']
for days, fruits, drinks, desserts in zip( days, fruits, drinks, desserts ):
    print(days, ": drinks", drinks, '-eat', fruits, '-enjoys', desserts)