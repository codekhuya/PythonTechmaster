'''
for i in range(1, 10):
    print("--------------------")
    for j in range (1, 10):
        print("%2d *%2d = %2s" % (i, j , i*j))
'''

students = [("Alejandro", ["CompSci", "Physics"]),
            ("Justin", ["Math", "CompSci", "Stats"]),
            ("Ed", ["CompSci", "Accounting", "Economics"]),
            ("Margot", ["InfSys", "Accounting", "Economics", "ComLaw"]),
            ("Peter", ["Sociology", "Economics", "Law", "Stats", "Music"])]

for (name, subjects) in students:
    print(name, "takes", len(subjects), "courses")

counter = 0
for (name, subjects) in students:
    for s in subjects:
        if s == "CompSci":
            counter += 1
print("The num ber of students taking CompSci is", counter)
