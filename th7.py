#câu 7.3:
file=open("tep.txt","r")
a=file.read()
print("noi dung file la: ",a)
file.close()
#câu 7.7:
file=open("tep.txt","r")
s=0
for line in file:
    s=s+1
print("so dong cua file la: ",s)
file.close()
#cau 7.8
a=input('nhap noi dung danh sach: ')
file=open("tep.txt","a")
file.write(a)
file.close()
#cau 7.9
file=open("tep.txt","r")
a=file.read()
fi=open("abc.txt","a")
fi.write(a)
fi.close()
file.close()
#cau 7.10
file=open("tep.txt","r")
a=file.read()
b=[x for x in a.split(' ')]
c=b[0]
for i in b:
    if i>c:
        c=i
print('chu dai nhat trong van ban la: ',c)

