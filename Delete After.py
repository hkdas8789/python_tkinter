#
# # Date - 26-01-2022
# from tkinter import *
# from PIL import Image, ImageTk
# root=Tk()
# root.geometry("800x500")
# root.minsize(400,300)
# root.maxsize(1200,650)
#
# # Images here
# '''pic_file=Image.open("bird.jpg")  # Enter photo name here .
# image_=ImageTk.PhotoImage(pic_file)
# label_image=Label(image=image_)
# label_image.pack()
# '''
#
# # Frame here
# f1=Frame(bg="Orange",borderwidth=10,relief=SUNKEN)
# f1.pack(side=TOP,fill=X)
# f2=Frame(bg="White",borderwidth=10,relief=SUNKEN)
# f2.pack(side=TOP,fill=X)
# f3=Frame(bg="Green",borderwidth=10,relief=SUNKEN)
# f3.pack(side=TOP,fill=X)
#
#
# # Label here
# '''la0=Label(f1,text=" Happy  ",bg="Orange",fg="Black",font="mango 20 bold")
# la0.pack(side=TOP,anchor="nw")
#
# la1=Label(f2,text="republic",bg="White",fg="Black",font=("Mango",20,"bold"))
# la1.pack(side=TOP,anchor='nw')
#
# la2=Label(f3,text='    Day   ',bg="Green",fg="Black",font="mango 20 bold")
# la2.pack(side=TOP,anchor='nw')'''
# # Buttons functions command
# def Button_1():print("This is Button 1 .")
# def Button_2():print("This is Button 2 .")
# def Button_3():print("This is Button 3 .")
# # Button here
# b1=Button(f1,text="Button 1",bg="Black",fg="Cyan",font="mango 20 bold",padx=100,command=Button_1)
# b1.pack()
# b2=Button(f2,text="Button 2",bg="Black",fg="Cyan",font="mango 20 bold",padx=100,command=Button_2)
# b2.pack()
# b3=Button(f3,text="Button 3",bg="Black",fg="Cyan",font="mango 20 bold",padx=100,command=Button_3)
# b3.pack()
#
#
# if __name__ == '__main__':
#     root.mainloop()


'''from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry ("800x400")
root.minsize(500,300)
def speak(string):
    from win32com.client import Dispatch
    s=Dispatch("SAPI.SpVoice")
    s.Speak(string)
root.title("Revision")

# i_m=Image.open('7.jpg')
# i_m_p=ImageTk.PhotoImage(i_m)
# la=Label(image=i_m_p)
# la.pack()
def a():print("HELLO WORLD");speak("HELLO WORLD")
def b():print("Hello world");speak("Hello world")
f1=Frame(root,bg="Green",borderwidth=20,relief=RIDGE)
f1.pack(side=RIGHT,anchor='nw')
l=Button(f1,text="HELLO WORLD",background="Green",fg="Dark blue",padx=10,font="mango 30 bold",command=a)
l.pack()

f2=Frame(root,bg="Green",borderwidth=20,relief=RIDGE)
f2.pack(side=RIGHT,anchor='nw')
l1=Button(f2,text="Hello world",background="Cyan",fg="Black",padx=10,font="mango 30 bold",command=b)
l1.pack()

root.mainloop()'''


from tkinter import *
def speak(string):
    from win32com.client import Dispatch
    Dispatch("SAPI.SpVoice").Speak(string)
root=Tk()
root.title("Normal")





def he():
    speak(f"Hello sir, Your name is {i}.")
    print(f"Hello sir, Your name is {i}.")

i=input("Enter your name:-")

f2=Frame(root,bg="Dark Blue",borderwidth=10,relief=RIDGE)
f2.pack(side=RIGHT,anchor="ne")
b2=Button(f2,bg="Black",fg="Cyan",font="mango 20 bold",text=f"Your name is {i}")
b2.pack()
f1=Frame(root,bg="Black",borderwidth=10,relief=RAISED)
f1.pack(side=LEFT,anchor="nw")
b1=Button(f1,bg="Cyan",fg="Grey",font="mango 10 bold",text="Click here",command=he)
b1.pack()

if __name__ == '__main__':
    root.mainloop()