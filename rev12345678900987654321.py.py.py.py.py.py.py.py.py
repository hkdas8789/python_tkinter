
from tkinter import *
rt=Tk()
F1=Frame(rt)
rt.title("Offline Google")
F1.grid(row=0,column=4)
l1=Label(F1,text="G",fg="Blue",font="mango 50 bold")
l1.grid(row=0,column=1)
l2=Label(F1,text="o",fg="Red",font="mango 50 bold")
l2.grid(row=0,column=2)
l3=Label(F1,text="o",fg="Yellow",font="mango 50 bold")
l3.grid(row=0,column=3)
l4=Label(F1,text="g",fg="Blue",font="mango 50 bold")
l4.grid(row=0,column=4)
l5=Label(F1,text="l",fg="Green",font="mango 50 bold")
l5.grid(row=0,column=5)
l6=Label(F1,text="e",fg="Red",font="mango 50 bold")
l6.grid(row=0,column=6)
l7=Label(F1,text="T",fg="Black",font="mango 6 bold",pady=70)
l7.grid(row=0,column=7)
l8=Label(F1,text="M",fg="Black",font="mango 6 bold",pady=70)
l8.grid(row=0,column=8)

def Search():
    global i
    print(f"User search '{i.get()}'in fake google 😂.")

i=StringVar()
Entry(textvariable=i,font="mango 13 bold").grid(row=2,column=4)
Button(text="Search",font="mango 10 bold",command=Search).grid(row=2,column=5)



rt.mainloop()

































