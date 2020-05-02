#3.3
def say_hello():
    a="hello"
    print(a)
print(say_hello())
#3.4:
n=int(input("nhap so n"))
def kiem_tra(n):
    if n%2==0:
       print("so chan")
    else:
       print("so le")
kiem_tra(n)
#3.10
import math
r=int(input("nhap ban kinh r"))
def tinh(r):
    c=2*r*math.pi;
    s=math.pi*r*r;
    print("chu vi la: ",c)
    print("dien tich la: ",s)
tinh(r)
#3.11
t=int(input("nhap lai suat"))
n=int(input("nhap so tien goc"))
k=int(input("nhap so thang gui"))
def tinh_lai(t,n,k):
    s=n;
    for i in range(0,k):
        s=s+n*t/100;
    print("so tien nhan duoc: ",s)
tinh_lai(t,n,k)
       
