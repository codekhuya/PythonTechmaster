'''
Bài tập: Đội bóng Barcelona trong biên chế có 25 cầu thủ.
Đội hình chính thức ra sân chỉ có 11 cầu thủ.
Huấn luyện viên sẽ phân phối đội hình
1- 4 - 4 -2 có nghĩa là:
1 thủ môn
4 hậu vệ  (2 trụ - 2 biên)
4 tiền vệ
2 tiền đạo

Hãy xây dựng một đoạn mã giúp huấn luyện viên Luis Enrique
 chọn được đội hình 11 cầu thủ theo đội hình 1-4-4-2 đáp ứng
 tiêu chí vừa ngẫu nhiên nhưng vừa hợp lý (không thể có 2 thủ môn cùng ra sân)
'''

import random

thu_mon = (1, 2) #2 thủ môn
hau_ve = (3, 4, 5, 6, 16, 17, 18, 19, 23) #9 hậu vệ
tien_ve = (11, 12, 13, 14, 15, 20, 21, 22, 24) #9 tiền vệ
tien_dao = (7 ,8 ,9, 10, 25) #5 tiền đạo

print("======== Danh sach cau thu ra san theo doi hinh 1-4-4-2 ========")
print("Thu mon so: ", random.choice(thu_mon))
print("4 Hau ve:", random.sample(hau_ve, 4))
print("4 Tien ve:", random.sample(tien_ve, 4))
print("2 Tien dao:", random.sample(tien_dao, 2))
