#4.2
s=input('nhap chuoi: ')
for i in s:
    if i==' ':
       continue
    else:
        print(i)

#4.3
s=input('nhap chuoi: ')
print(s.upper())
#4.5
ds=input('danh sach: ').split()
print(ds)
i=len(ds)
while 1<=i:
    print(ds[i-1])
    i=i-1;
#4.6
n=input('nhap ten nguoi').split()
i=len(n)
print("ho la",n[0])
print("ten la",n[i-1])
#4.7
n=input('nhap chuoi')
for i in range(0,len(n)):
    if n[i].isdigit=='true':
        n[i]=3;
print(n)
#4.15
ds=input('danh sach: ').split()
ds.sort()
print(ds)
#4.21
value = []
items=[x for x in input("Nhập các số nhị phân: ").split(',')]
for p in items:
 intp = int(p, 2)
 if not intp%5:
 value.append(p)
print (','.join(value))
#4.22
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
 values.append(s)
print (",".join(values))
#4.23
s = input("Nhập câu của bạn: ")
d={"DIGITS":0, "LETTERS":0}
for c in s:
 if c.isdigit():
 d["DIGITS"]+=1
 elif c.isalpha():
 d["LETTERS"]+=1
 else:
 pass
print ("Số chữ cái là:", d["LETTERS"])
print ("Số chữ số là:", d["DIGITS"])
#4.24
s = input("Nhập câu của bạn: ")
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print ("Chữ hoa:", d["UPPER CASE"])
print ("Chữ thường:", d["LOWER CASE"])


