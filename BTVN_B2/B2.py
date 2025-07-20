def tinh_thue(luong):
    if luong > 15000000:
        return luong * 0.3
    elif luong >= 7000000:
        return luong * 0.2
    elif luong > 0:
        return luong * 0.1
    else:
        return 0

luong = int(input("Nhập lương: "))
thue = tinh_thue(luong)
thu_nhap_rong = luong - thue

print(f"Thuế: {int(thue)} Thu nhập: {int(thu_nhap_rong)}")
