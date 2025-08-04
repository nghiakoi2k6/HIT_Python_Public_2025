A = {'SV01', 'SV02', 'SV03'}
B = {'SV03', 'SV04', 'SV05'}

print("Bàn 1:", A)
print("Bàn 2:", B)

both = A & B
print("Đăng ký cả 2 bàn:", both if both else "Không có")

all_students = A | B
print("Tổng hợp đăng ký:", all_students)

only_A = A - B
print("Chỉ bàn 1:", only_A)
