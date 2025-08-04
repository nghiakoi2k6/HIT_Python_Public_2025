n_m_input = input("Nhập n và m (số phần tử của mảng và tập A, B): ")
n, m = map(int, n_m_input.split())

arr_input = input(f"Nhập {n} phần tử của mảng, cách nhau bằng khoảng trắng: ")
arr = list(map(int, arr_input.split()))

A_input = input(f"Nhập {m} phần tử của tập A (bạn thích): ")
A = set(map(int, A_input.split()))

B_input = input(f"Nhập {m} phần tử của tập B (bạn không thích): ")
B = set(map(int, B_input.split()))

happiness = 0
for x in arr:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1

print("Tổng mức độ hạnh phúc là:", happiness)
