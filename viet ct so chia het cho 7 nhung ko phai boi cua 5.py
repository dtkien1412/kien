j=[]
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        j.append(str(i))
print("cac so chia het cho 7 ma ko phai boi cua 5 la:",','.join(j))
