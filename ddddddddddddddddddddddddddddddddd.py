#
#
# from tkinter import *
# root=Tk()
# root.geometry("600x400")
# root.minsize(300,200)
# root.title("GUI")
#
# # def c1():
# #     print(f"Name is {.get()}.")
#
#
#
#
#
#
# ente=Entry(textvariable=StringVar())
# ente.grid(row=0,column=1)
#
#
#
#
#
#
#
# b1=Button(text="Submit")
# b1.grid(row=3,column=1)
#
#
#
#
#
#
# if __name__ == '__main__':
#     root.mainloop()

# from sys import version
# print(version)
"""
from tkinter import *
root=Tk()
root.title("GUI")
root.geometry("800x500")
root.minsize(500,400)
f1=Frame(root,bg="Black",borderwidth=1,relief=RAISED)
f1.grid()
l1=Label(f1,text="Name",fg="Black",bg="Red",font="mango 30 bold",padx=5)
l1.grid()
#
i=StringVar()


f2=Frame(root,bg="Dark blue",borderwidth=2,relief=RAISED)
f2.grid(row=0,column=1)
e=Entry(f2,textvariable=i,font="mango 30 bold",fg="White",bg="Dark blue")
e.grid(padx=10)



def f_v():
    print(f"User name is {i.get()}.")

bu1=Button(root,text="Submit",fg="Black",bg="yellow",borderwidth=5,relief=SUNKEN,font="mango 30 bold",command=f_v,padx=150)
bu1.grid(row=1,column=1)


button_for_quiting=Button(text="Quit",fg="Black",bg="Purple",borderwidth=5,relief=SUNKEN,font="mango 20 bold",command=quit,pady=15,padx=25)
button_for_quiting.grid(row=1)

if __name__ == '__main__':
    root.mainloop()
"""

# try:
#     while True:
#         i=float(input("Enter 1st number\n:-"))
#         ii=float(input("Enter 2nd number\n:-"))
#         print(f"The  multipal of {i} & {ii} is {i*ii}")
# except Exception as e:
#     print(e)
# finally:
#     print("\n\n\t\tThank you\n\n\t\t")


def happy(year):
    try:
        from random import randint, choice
        from time import sleep
        while True:
            a = randint(10, 160)
            space = randint(2, 20)
            f = ["   ", "    ", "   ", f"Happy new year {year}", "    ", "    ", "    ", "    "]
            c = choice(f)
            print("  "*space, c, " " * a, "*")
            #print(c)
            sleep(0.1)
    except Exception as e:
        print(e)
happy(2023)