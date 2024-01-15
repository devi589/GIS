#phần a:
'''Hàm isPerfectSquare, trả về kq nếu n=0 hoặc nếu bình phương (giá trị nguyên của n mũ 0,5) bằng n
thì n là số chính phương và hàm trả về'''

def isPerfectSquare(n):
    return n == 0 or int(n ** 0.5) ** 2 == n

#phần b:
'''Dãy Fibonacci là dãy vô hạn các số tự nhiên bắt đầu bằng hai phần tử 0 và 1 hoặc 1 và 1,
các phần tử sau đó được thiết lập theo quy tắc mỗi phần tử luôn bằng tổng hai phần tử trước nó
Hàm này kiểm tra xem một số n có phải là số Fibonacci hay không
Nó sử dụng một vòng lặp while để tính các số Fibonacci cho đến khi số Fibonacci vượt quá n
Nếu n là một số Fibonacci, hàm trả về n'''

def isFibo(n):
    f0, f1, fn = 0, 1, 1
    while f0 <= n:
        if f0 == n:
            return n
        else:
            f0 = f1
            f1 = fn
            fn = f0 + f1
#phần c 
def Toatl(n):
    sum = 0;
    while n > 0 : #trong khi điều kiện đúng 
        sum = sum + n % 10; #tổng = tổng + n chia 10 lấy phần dư
        n = int(n / 10); #lấy phần nguyên của n/10 
    return sum;

#Nhập n nguyên
n = int(input("Nhap n: "))

# Kiểm tra điều kiện của n (WEEK 3)
while n < 0 or n > 1000:
    print("Gia tri n khong hop le!")
    n = int(input("Nhap n: "))

#Khởi tạo danh sách lưu trữ các số chính phương (WEEK 5)
list1 = []

'''Lặp qua các số từ 0 đến (n-1)
Gọi hàm isPerfectSquare() để kiểm tra xem i có phải là số chính phương hay không.
Nếu i là số chính phương, chương trình sẽ thêm i vào ds list1'''

for i in range(0,n):
    if isPerfectSquare(i):
        list1.append(i) #thêm i vào cuối danh sách
print("Danh sach cac so chinh phuong nho hon n la:", list1)

#Danh sách lưu trữ các số vừa là số chính phương, vừa là số Fibonacci
list2 = []

'''Lặp qua các số từ 0 đến (n-1)
Gọi hàm isPerfectSquare() và isFibo() để kiểm tra xem i có phải là số chính phương và số Fibo hay không.
Nếu i là số chính phương và số Fibo, chương trình sẽ thêm i vào ds list'''

for i in range(0, n):
    #Sử dụng nếu không bằng None để xác định giá trị
    if isPerfectSquare(i) and isFibo(i) !=None:
        list2.append(i)
print("Danh sach cac sa vua la so chinh phuong, vua la so Fibonacci nho hon n la:", list2)

#Danh sách giá trị lần lượt của tổng
list3 = []

'''Lặp qua các số từ 10 đến (n-1)
Gọi hàm isPerfectSquare() để kiểm tra xem i có phải là số chính phương hay không.
Nếu i là số chính phương, tổng các chữ số sẽ đc tính bằng hàm Toatl(i)
Sau đó chương trình sẽ thêm tổng vào ds list'''

for i in range(10,n):#Vì đề bài yêu cầu các số có 2 chữ số nên chạy bắt đầu từ 10 đến n là đến giá trị (n-1)
    if isPerfectSquare(i): #từ phần a
        tong = Toatl(i) #từ phần c
        list3.append(tong) 
print("Danh sach gia tri lan luot cua tong cac chu so cua so chinh phuong co 2 chu so tro len:", list3)
