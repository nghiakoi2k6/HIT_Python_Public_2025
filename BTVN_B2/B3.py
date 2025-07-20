n = int(input("n = "))
sum = 0
c = 0
temp = n
while temp > 0:
    c += 1
    sum += temp % 10
    temp //= 10
print(f"so chu so: {c} tong: {sum}")