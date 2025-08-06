lst = input("Nhập danh sách chuỗi: ")

tmp = set()

for s in lst:
    parts = s.split()
    for p in parts:
        tmp.add(p)

result_list = list(tmp)

print("Danh sách mới:", result_list)
