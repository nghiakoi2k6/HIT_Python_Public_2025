# Nhập số lượng phần tử
n = int(input("Nhập số phần tử n: "))

# Khởi tạo list rỗng và nhập giá trị
a = []
for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(val)

# Nhập số X và đếm số lần xuất hiện
X = int(input("Nhập số X: "))
count_X = a.count(X)
print(f"Số {X} xuất hiện {count_X} lần trong list.")

# Đảm bảo list đủ dài để thay thế từ vị trí 2 đến 7
if len(a) >= 8:
    a[2:8] = [8, 5, 4, 0, 1, 3]
else:
    print("List không đủ dài -> thêm giá trị 0 vào cuối để đủ độ dài")
    while len(a) < 8:
        a.append(0)
    a[2:8] = [8, 5, 4, 0, 1, 3]

# In list sau khi thay thế
print("List sau khi thay thế:", a)

# Tìm số lớn nhất và nhỏ nhất
max_val = max(a)
min_val = min(a)
print(f"Số lớn nhất trong list là: {max_val}")
print(f"Số nhỏ nhất trong list là: {min_val}")

# Nhập số Y và chèn vào đầu list
Y = int(input("Nhập số Y: "))
a.insert(0, Y)
print("List sau khi chèn Y vào đầu:", a)

# Kiểm tra list có sắp xếp tăng, giảm hay không
if a == sorted(a):
    print("TĂNG")
elif a == sorted(a, reverse=True):
    print("GIẢM")
else:
    print("NO")
