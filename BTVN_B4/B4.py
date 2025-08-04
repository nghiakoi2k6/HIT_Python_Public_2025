n = int(input("Nhập số phần tử: "))
a = [input(f"Phần tử {i+1}: ") for i in range(n)]

b = tuple(a)
print("Tuple b:", b)

dem_so = sum(1 for x in b if x.isdigit())
print("Số phần tử dạng số:", dem_so)
