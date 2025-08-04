t = ('1', '2', '3', '4', '5')

t_new = tuple(map(int, t))
print("Tuple sau khi chuyển:", t_new)

avg = sum(t_new) / len(t_new)
print("Trung bình cộng:", avg)
