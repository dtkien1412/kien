#5.5
n=int(input('nhap so luong n '))
s=[]
for i in range(0,n):
    a=str(input('nhap phan tu list '))
    s.append(a)
b=max(s)
print("phan tu lon nhat",b)
print("phan tu nho nhat",min(s))
#5.6 tim vị trí của max
for i in range(0,n):
    if s[i]==b:
        print("vị trí của max là : ",i)
#5.7
        
