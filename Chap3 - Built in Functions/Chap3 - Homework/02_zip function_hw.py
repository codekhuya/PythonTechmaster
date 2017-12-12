'''
Bài tập về nhà cho 2 list x và y. Hãy lập trình tạo ra một list
chỉ chứa các tuple thỏa mãn điều kiện tổng 2 phần tử trong tuple <= 10
x = [9, 2, 3, 2, 1, 2]
y = [4, 5, 6, 7, 12, 15]
'''

x = [9, 2, 3, 2, 0, 3, 1, 2, 3]
y = [4, 5, 6, 7, 1, 4, 12, 15, 4]
zipped = list(zip(x, y))
for i in range(0, zipped.__len__()):
    if(sum(zipped[i]) <= 10):
        print(zipped[i])