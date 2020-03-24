import math

#Nhap vao he so
a=int(input("nhap gia tri a: "))
b=int(input("nhap gia tri b: "))
c=int(input("nhap gia tri c: "))

#kiem tra pt
if a==0:
    print("pt la ko phai pt bac 2")
else:
    #tinh nghiem pt bac 2
    denta=b*b-4*a*c
    if (denta<0):
        print("phuong trinh vo nghiem")
    elif (denta==0):
        x=-b/(2*a)
        print("pt co nghiem kep x la: ",x)
    else:
        x1=((-b-math.sqrt(denta))/(2*a));
        x2=((-b+math.sqrt(denta))/(2*a));
        print("pt co nghiem x1 la: ",x1)
        print("pt co nghiem x2 la: ",x2)
