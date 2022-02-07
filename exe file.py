from tkinter import *

root = Tk()
root.geometry("526x257")
root.minsize(526,257)
root.maxsize(526,257)
def printdet():
    global i1, i2, i3, i4, i5, ivr
    if True:
        # print(
        #     f"[ User name is {i1.get()} , Email is {i2.get()} , Password is {i3.get()} , Phone number is {i4.get()} , Address {i5.get()} ]")
        with open("User Value.txt", 'a') as f:
            f.write(f"[ User name is {i1.get()} , Email is {i2.get()} , Password is {i3.get()} , Phone number is {i4.get()} , Address {i5.get()} ]\n\n")
def files():
    f=open('user value.txt')
    content=f.read()
    print(content)
    f.close()


F1 = Frame(root, bg='Black', borderwidth=10, relief=RAISED)
F1.grid(row=0, column=2)

l0 = Label(F1, text='Welcome to register form', bg="Black", fg='Yellow', pady=15, font='mango 15 bold')
l0.grid(row=0, column=2)

l1 = Label(F1, text='Name', bg='Black', font='mango 10 bold', fg='Cyan', pady=5)
l1.grid(row=1, column=1)

l2 = Label(F1, text='Email', bg='Black', font='mango 10 bold', fg='Cyan', pady=5)
l2.grid(row=2, column=1)

l3 = Label(F1, text='Password', bg='Black', font='mango 10 bold', fg='Cyan', pady=5)
l3.grid(row=3, column=1)

l4 = Label(F1, text='Phone Number', bg='Black', font='mango 10 bold', fg='Cyan', pady=5)
l4.grid(row=4, column=1)

l5 = Label(F1, text='Address', bg='Black', font='mango 10 bold', fg='Cyan', pady=5)
l5.grid(row=5, column=1)

i1 = StringVar()
i2 = StringVar()
i3 = StringVar()
i4 = StringVar()
i5 = StringVar()
ivr = IntVar()

e1 = Entry(F1, textvariable=i1, font='mango 10 bold')
e1.grid(row=1, column=2)

e2 = Entry(F1, textvariable=i2, font='mango 10 bold')
e2.grid(row=2, column=2)

e3 = Entry(F1, textvariable=i3, font='mango 10 bold')
e3.grid(row=3, column=2)

e4 = Entry(F1, textvariable=i4, font='mango 10 bold')
e4.grid(row=4, column=2)

e5 = Entry(F1, textvariable=i5, font='mango 10 bold')
e5.grid(row=5, column=2)




Checkbutton(F1, text='Are all right?', fg='Cyan', bg='Black', font='mango 10 bold', command=ivr).grid(row=6, column=2)

Button(F1,text="file data",font="mango 10 bold",bg="Blue",fg="Cyan",command=files).grid(row=6,column=5)  #############################

Button(F1, text='Submit', fg='Cyan', bg='Blue', font='mango 10 bold', command=printdet).grid(row=6, column=3)

Button(F1, text='Quit', fg='Cyan', bg='Blue', font='mango 10 bold', command=quit).grid(row=6, column=4)


root.mainloop()