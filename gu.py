# TODO:  pip install pywin32
# TODO------------------------------------------------------------------------------------------------------------------
from tkinter import*
from win32com.client import Dispatch
PASSWORD = 2022
root = Tk()
# TODO: Creating window
Title = "GUI form"
root.title(Title)
Height = 296
Width = 749
root.geometry(f"{Width}x{Height}")
root.minsize(Width,Height)
root.maxsize(Width,Height)
with open("uv",'a') as f:
    f.write(" ")
#TODO: Create Speak function
def speak(str):
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
# TODO: Open file in append mode
def submit():
    global f1,i1,i2,i3,i4,i5,i6
    if i1.get() and i2.get() and i3.get() and i4.get() and i5.get() and i6.get():
        with open("uv.txt","a") as fi1:
            fi1.write(f"[Name - {i1.get()} ,Email id - {i2.get()} ,Password - {i3.get()} ,Contact Number - {i4.get()} ,Date of birth - {i5.get()} and Height - {i6.get()}]\n")
        Label(f1, text="                                                          ", font="mango 10 bold", pady=20,bg="Lime").grid(row=9, column=2)
        Label(f1,text="Your data has saved",fg="Teal",font="Mango 10 bold",bg="Lime").grid(row=9,column=2)
    else:
        lv = Label(f1, text="                                                          ", font="mango 10 bold", pady=20,bg="Lime")
        lv.grid(row=9, column=2)
        ln = Label(f1,text="Fill all details",font="mango 10 bold",fg="Teal",pady=20,bg="Lime")
        ln.grid(row=9,column=2)
def clean():
    Label(f1, text="                                                                   ", font="mango 10 bold", pady=20,bg="Lime").grid(row=9, column=2)
def fil():
    if password.get()==str(PASSWORD):
        rd = open('uv.txt')
        content = rd.read()
        print(content)
        rd.close()
    else:
        ln = Label(f1, text="                                                           ", font="mango 10 bold", pady=20,bg="Lime")
        ln.grid(row=9, column=2)
        la = Label(f1, text="You can't open file data", font="mango 10 bold", pady=20,fg="Teal",bg="Lime")
        la.grid(row=9, column=2)
def speak_file():
    if password.get()==str(PASSWORD):
        rd = open('uv.txt')
        content = rd.read()
        speak(content)
        rd.close()
    else:
        ln = Label(f1, text="                                                           ", font="mango 10 bold",pady=20,bg="Lime")
        ln.grid(row=9, column=2)
        la = Label(f1, text="Try again!",fg="Teal", font="mango 10 bold", pady=20,bg="Lime")
        la.grid(row=9, column=2)
# TODO: Frame's
f1 = Frame(root,borderwidth=3,relief="sunken",bg="Lime")
f1.grid(row=0,column=3)
Label(f1, text="                                                                   ", font="mango 10 bold", pady=20).grid(row=9, column=2)
# TODO: Label's
l0 = Label(f1,text="Welcome",fg="Red",font="Mango 15 bold",pady=10,bg="Lime") #TODO: Welcome here
l0.grid(row=0,column=2)
l1 = Label(f1,text="Name",fg="Black",font="Mango 10 bold",bg="Lime")
l1.grid(row=1,column=1)
l2 = Label(f1,text="Email id",fg="Black",font="Mango 10 bold",bg="Lime")
l2.grid(row=2,column=1)
l3 = Label(f1,text="Password",fg="Black",font="Mango 10 bold",bg="Lime")
l3.grid(row=3,column=1)
l4 = Label(f1,text="Contact No.",fg="Black",font="Mango 10 bold",bg="Lime")
l4.grid(row=4,column=1)
l5 = Label(f1,text="D.O.B",fg="Black",font="Mango 10 bold",bg="Lime")
l5.grid(row=5,column=1)
l6 = Label(f1,text="Height",fg="Black",font="Mango 10 bold",bg="Lime")
l6.grid(row=6,column=1)
l7 = Label(f1,text="Enter password to open file data",fg="Black",font="Mango 10 bold",bg="Lime")
l7.grid(row=7,column=1)
# TODO: input's
i1 = StringVar()
i2 = StringVar()
i3 = StringVar()
i4 = StringVar()
i5 = StringVar()
i6 = StringVar()
password = StringVar()
# TODO: Entry point
e1 = Entry(f1,textvariable=i1,fg="Blue",font="Mango 10 bold")
e1.grid(row=1,column=2)
e2 = Entry(f1,textvariable=i2,fg="Blue",font="Mango 10 bold")
e2.grid(row=2,column=2)
e3 = Entry(f1,textvariable=i3,fg="Blue",font="Mango 10 bold",show="*")
e3.grid(row=3,column=2)
e4 = Entry(f1,textvariable=i4,fg="Blue",font="Mango 10 bold")
e4.grid(row=4,column=2)
e5 = Entry(f1,textvariable=i5,fg="Blue",font="Mango 10 bold")
e5.grid(row=5,column=2)
e6 = Entry(f1,textvariable=i6,fg="Blue",font="Mango 10 bold")
e6.grid(row=6,column=2)
e7 = Entry(f1,textvariable=password,fg="Blue",font="Mango 10 bold",show="*")
e7.grid(row=7,column=2)
#TODO: Button's
b1 = Button(f1,text="Submit",font="Mango 10 bold",fg="Green",command=submit)
b1.grid(row=8,column=4)
b2 = Button(f1,text="File data",font="Mango 10 bold",fg="Green",command=fil)
b2.grid(row=8,column=5)
b3 = Button(f1,text="Clean",font="Mango 10 bold",fg="Green",command=clean)
b3.grid(row=8,column=7)
# TODO: creating password button
b4 = Button(f1,text="Speak data",font="Mango 10 bold",fg="Green",command=speak_file)
b4.grid(row=8,column=6)
#TODO: Fill space
Label(f1, text="                                                                   ", font="mango 10 bold", pady=20,bg="Lime").grid(row=9, column=2)
if __name__ == '__main__':
    root.mainloop()