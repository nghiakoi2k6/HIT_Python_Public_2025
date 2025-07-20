xu = int(input("Nhập xu: "))

chai = xu // 28  
sum = chai      
vo = chai       

while vo >= 3:
    doi = vo // 3         
    sum += doi             
    vo = vo % 3 + doi      

print(f"Số chai bia có thể mua được là: {sum}")
