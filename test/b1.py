t = tuple(map(int, input("Nhập các số (cách nhau bằng khoảng trắng): ").split()))

result = set()

for num in set(t): 
    count = t.count(num)
    if count % 5 == 0 and num % 10 != 0:  
        result.add(num)

print("Kết quả:", result)
