def check(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)
def checkNgay(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]: return 31
    elif thang in [4, 6, 9, 11]: return 30
    elif thang == 2:
        return 29 if check(nam) else 28
    else:
        return "thang khong hop le."

thang = int(input("nhap thang: "))
nam = int(input("nhap nam: "))

songay = checkNgay(thang, nam)
print (f"so ngay trong thang {thang}/{nam} la: {songay}")