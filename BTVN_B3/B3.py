s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")

reverse_s1 = s1[::-1]
print("Đảo ngược của s1:", reverse_s1)

while True:
    a = int(input(f"Nhập số nguyên a >= 1 "))
    b = int(input(f"Nhập số nguyên b(a < b <= {len(s2)}): "))
    if 1 <= a < b <= len(s2):
        break
    else:
        print("Giá trị a, b không hợp lệ, nhập lại!")
s2_sau = s2[:a] + s2[a:b+1][::-1] + s2[b+1:]
print(s2_sau)

s3 = ''.join([char for i, char in enumerate(s1) if i % 2 == 0])
print(s3)

length = min(len(s1), len(s2))
s4 = ' '

for i in range(length):
    s4 += s1[i] + s2[i]

#nối phần còn lại
if len(s1) > length:
    s4 += s1[length:]
if len(s2) > length:
    s4 += s2[length:]

print("Chuỗi s4 (đan xen s1 và s2):", s4)
