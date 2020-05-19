#bai 8.3:
import turtle
colors=["red","green","blue"]
painter=turtle.Turtle()
painter.pensize(3)
for i in range(4):
    for i in range(0,3):
        color=colors[i]
        painter.pencolor(color)
        painter.circle(100)
        painter.right(30)
        painter.left(60)
        painter.setposition(0,0)
#bai 8.4:
from tkinter import *
window=Tk()
window.title("welcome")
window.geometry('350x200')
lb=Label(window,text="hello")
def click():
    lb.configure(text="bye")
bt=Button(window,text="click me",bg="red",font=('time',20),command=click)
bt.grid(column=1,row=0)
window.mainloop()
#bai 8.8 a:
from tkinter import *
tk=Tk()
tk.title('welcome')
tk.geometry('350x350')
lb1=Label(tk,text='Dinh Trung Kien',font=('time',20))
lb1.place(x=100,y=50)
lb2=Label(tk,text='msv:18575103010037',font=('time',20))
lb2.place(x=100,y=100)
lb3=Label(tk,text='date:14/03/200',font=('time',20))
lb3.place(x=100,y=150)
tk.mainloop()
#bai 8.8 b:
from tkinter import *
tk=Tk()
tk.title('welcome')
tk.geometry('350x350')
var1=BooleanVar()
var1.set(False)
cb1=Checkbutton(tk,text='first',variable=var1)
cb1.place(x=0,y=0)
var2=BooleanVar()
var2.set(False)
cb2=Checkbutton(tk,text='second',variable=var2)
cb2.place(x=0,y=50)
var3=BooleanVar()
var3.set(False)
cb3=Checkbutton(tk,text='third',variable=var3)
cb3.place(x=0,y=100)
def click():
    if var1.get()== True:
        lb1=Label(tk,text='1')
        lb1.place(x=200,y=0)
    if var2.get()== True:
        lb2=Label(tk,text='2')
        lb2.place(x=200,y=50)
    if var3.get()== True:
        lb3=Label(tk,text='3')
        lb3.place(x=200,y=100)
bt=Button(tk,text='click me',command=click)
bt.place(x=100,y=50)
tk.mainloop()

