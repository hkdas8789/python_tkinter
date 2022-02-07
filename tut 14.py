from tkinter import *
root=Tk()
def resize():
    global Width,Height
    print(f"Window Update.")
    root.geometry(f"{Width.get()}x{Height.get()}")
root.geometry(f"{250}x{85}")
f1=Frame(root,bg="Dark blue",borderwidth=5,relief=SUNKEN)
f1.grid(row=1,column=3)
Width=StringVar()
Height=StringVar()
Label(f1,text="Width ",font="mango 10 bold",bg='Dark blue',fg="Light blue").grid(row=1,column=1)
Label(f1,text="Height",font="mango 10 bold",bg='Dark blue',fg="Light blue").grid(row=2,column=1)
Entry(f1,textvariable=Width,font="mango 10 bold").grid(row=1,column=2)
Entry(f1,textvariable=Height,font="mango 10 bold").grid(row=2,column=2)
Button(f1,text="Apply",font="mango 10 bold",command=resize).grid(row=3,column=3)
root.mainloop()

exit()
# from tkinter import *
# root=Tk()
# root.title("Events in Tkinter")
# root.geometry("644x334")
# def abhishek(event):
#     print(f"You clicked on the button at {event.x},{event.y} ")
#
# widget = Button(root,text="Click me please")
# widget.pack()
#
# widget.bind('<Button-1>',abhishek) #TODO print the event.
# widget.bind('<Double-1>',quit)  #TODO quit the GUI.
#
# root.mainloop()