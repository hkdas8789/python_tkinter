'''
from tkinter import*
root=Tk()
root.geometry('600x400')
root.minsize(600,400)
root.maxsize(600,400)


def i():print(1)
def ii():print(2)
def iii():print(3)
def iv():print(4)
def v():print(5)
def vi():print(6)
def vii():print(7)
def viii():print(8)
def ix():print(9)
def o():print(0)




frame1 = Frame(root,borderwidth=6,background='gray',relief=RIDGE)
frame1.pack(side=LEFT,anchor='nw')
Button(frame1,fg='black',text='1',font=('mango 10 bold'),pady=5,command=i).pack(side=LEFT)


frame2 = Frame(root,borderwidth=6,background='gray',relief=RIDGE)
frame2.pack(side=LEFT,anchor='nw')
Button(frame2,fg='black',text='2',font=('mango 10 bold'),pady=5,command=ii).pack(side=LEFT)


frame3 = Frame(root,borderwidth=6,background='gray',relief=RIDGE)
frame3.pack(side=LEFT,anchor='nw')
Button(frame3,fg='black',text='3',font=('mango 10 bold'),pady=5,command=iii).pack(side=LEFT)


frame4 = Frame(root,borderwidth=6,background='gray',relief=RIDGE)
frame4.pack(side=LEFT,anchor='nw')
Button(frame4,fg='black',text='4',font=('mango 10 bold'),pady=5,command=iv).pack(side=LEFT)


frame5 = Frame(root,borderwidth=6,background='gray',relief=RIDGE)
frame5.pack(side=LEFT,anchor='nw')
Button(frame5,fg='black',text='5',font=('mango 10 bold'),pady=5,command=v).pack(side=LEFT)


frame6 = Frame(root,borderwidth=6,background='gray',relief=RIDGE)
frame6.pack(side=LEFT,anchor='nw')
Button(frame6,fg='black',text='6',font=('mango 10 bold'),pady=5,command=vi).pack(side=LEFT)


frame7 = Frame(root,borderwidth=6,background='gray',relief=RIDGE)
frame7.pack(side=LEFT,anchor='nw')
Button(frame7,fg='black',text='7',font=('mango 10 bold'),pady=5,command=vii).pack(side=LEFT)


frame8 = Frame(root,borderwidth=6,background='gray',relief=RIDGE)
frame8.pack(side=LEFT,anchor='nw')
Button(frame8,fg='black',text='8',font=('mango 10 bold'),pady=5,command=viii).pack(side=LEFT)


frame9 = Frame(root,borderwidth=6,background='gray',relief=RIDGE)
frame9.pack(side=LEFT,anchor='nw')
Button(frame9,fg='black',text='9',font=('mango 10 bold'),pady=5,command=ix).pack(side=LEFT)


frame0 = Frame(root,borderwidth=6,background='gray',relief=RIDGE)
frame0.pack(side=LEFT,anchor='nw')
Button(frame0,fg='black',text='0',font=('mango 10 bold'),pady=5,command=o).pack(side=LEFT)


frameq = Frame(root,borderwidth=6,background='gray',relief=RIDGE)
frameq.pack(side=LEFT,anchor='nw')
Button(frameq,fg='black',text='Quit',font=('mango 10 bold'),pady=5,command=quit).pack(side=LEFT)

root.mainloop()'''

def i():print("phy-Gravity\nchy-Atoms & Molucless , Structor of atom \n bio - Why do we fill ill?")
def ii():print("This is our 2nd button.")
from tkinter import *
root=Tk()
root.geometry('800x500')
f1=Frame(root,bg="Black",borderwidth=10,relief=SUNKEN)
f1.pack(side=LEFT,anchor='nw')
b1=Button(f1,text='Science sybless',fg="Red",command=i,font="mango 20 bold")
b1.pack()

f2=Frame(root,bg="pink",borderwidth = 10 , relief = SUNKEN)
f2.pack(side=LEFT,anchor='nw')
b2=Button(f2,text="This is our 2nd button",font="mango 20 bold ",fg="black",command=ii)
b2.pack()

root.mainloop()