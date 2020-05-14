from tkinter import *
from tkinter import messagebox
def tinh():
    import math
    a=tb1.get()
    a=int(a)
    b=tb2.get()
    b=int(b)
    c=tb3.get()
    c=int(c)
    if a==0:
        messagebox.showinfo('ket qua','khong phai pt bac 2')
    else:
        denta=b*b-4*a*c
        if denta<0:
            messagebox.showinfo('ket qua','pt vo nghiem')
        elif denta==0:
            messagebox.showinfo('pt co nghiem la: ',(-b)/(2*a))
        else:
            messagebox.showinfo('pt co nghiem x1 la: ',(-b-math.sqrt(denta))/(2*a))
            messagebox.showinfo(",x2 la: ",(-b+math.sqrt(denta))/(2*a))
may_tinh=Tk()
may_tinh.title("giai phương trinh bac 2")
lb1=Label(may_tinh,text="nhap a")
lb1.pack()
tb1=Entry(may_tinh)
tb1.pack()
lb2=Label(may_tinh,text="nhap b")
lb2.pack()
tb2=Entry(may_tinh)
tb2.pack()
lb3=Label(may_tinh,text="nhap c")
lb3.pack()
tb3=Entry(may_tinh)
tb3.pack()
bt=Button(may_tinh,text="ket qua",command=tinh)
bt.pack()
may_tinh.mainloop
