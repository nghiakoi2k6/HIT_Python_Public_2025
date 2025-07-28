k = int(input("Nhập số lượng phần tử cảu list k: "))

a = []
for i in range(k):
    val = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(val)

n = int(input("Nhập số dòng của ma trận n: "))
m = int(input("Nhập số cột của ma trận m: "))

if n*m > k:
    print("NO")
else: 
    X = []
    c = 0
    for i in range(n):
        row = a[c : c+m]
        X.append(row)
        c += m 
    print("ma trận X: ")
    for row in X:
        print(row)
    print(X)
