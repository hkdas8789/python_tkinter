from tkinter import *
root = Tk()
def getvals():
    print("It works!")
root.geometry("700x400")
l1=Label(root,text="Welcome to Abhishek travels",font="comicsansms 13 bold",pady=10).grid(row=0,column=3)
name = Label(root,text="Name")
phone = Label(root, text="Phone")
gender = Label(root,text="Gender")
emergency = Label(root,text = "Emergency Contact")
paymentmode = Label(root,text="Payment Mode")


name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)


namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


nameentry = Entry(root,textvariable=namevalue)
phoneentry = Entry(root,textvariable=phonevalue)
genderentry = Entry(root,textvariable=gendervalue)
emergencyentry = Entry(root,textvariable=emergencyvalue)
paymentmodeentry = Entry(root,textvariable=paymentmodevalue)


nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

# Check box
foodservice = Checkbutton(text="Want to prebook your meals?",variable = foodservicevalue)
foodservice.grid(row=6,column=3)

# Button & packing it and assigning it a command
Button(text="Submit to Abhishek travels",command=getvals).grid(row=7,column=3)

root.mainloop()