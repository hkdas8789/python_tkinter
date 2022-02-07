# from tkinter import*
#
# root=Tk()
# root.geometry("1200x400")
# root.title("Fun")
#
# '''l=Label(text="This is our 1st GUI.",bg="Green",padx=10,pady=20,fg="Cyan",font="aimal 40 bold",borderwidth=20,relief=SUNKEN)
# l.pack(anchor='nw',padx=30,pady=60,fill='y')'''
#
#
# frame_1=Frame(root,bg="Grey",borderwidth=10,relief=SUNKEN)
# frame_1.pack(fill=X)
# label_1=Label(frame_1,text="This is our 1st frame",fg="Cyan",bg='Black',font="amial 50 bold",padx=500)
# label_1.pack()



from tkinter import*
root=Tk()
f0=Frame(root,bg='Dark blue',borderwidth=10,relief=RAISED)
f0.pack(side=TOP,fill="x")
l0=Label(f0,text="This is new exam time table for class 9",font="mango 35 bold",pady=40,bg="Dark blue",fg="Orange")
l0.pack()
f1=Frame(root,bg='Black',borderwidth=10,relief=SUNKEN)
f1.pack(side=TOP,fill='x')
l1=Label(f1,text="Date		Subject",font="mango 35 bold",bg='Black',fg='white',pady=20)
l1.pack()

f2=Frame(root,bg='Black',borderwidth=10,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
l2=Label(f2,text="21-01-2022    	English",bg='Black',fg='Light green',font="mango 35 bold")
l2.pack()

f3=Frame(root,bg='Black',borderwidth=10,relief=SUNKEN)
f3.pack(side=TOP,fill=X)
l3=Label(f3,text='24-01-2022   	Hindi',bg='Black',fg='Red',font="mango 35 bold")
l3.pack()

f4=Frame(root,bg='Black',borderwidth=10,relief=SUNKEN)
f4.pack(side=TOP,fill=X)
l4=Label(f4,text='25-01-2022	Maths',bg='Black',fg='Pink',font="mango 35 bold")
l4.pack()

f5=Frame(root,bg='Black',borderwidth=10,relief=SUNKEN)
f5.pack(side=TOP,fill=X)
l5=Label(f5,text='26-01-2022	Socal science',bg='Black',fg='yellow',font="mango 35 bold")
l5.pack()

f6=Frame(root,bg='Black',borderwidth=10,relief=SUNKEN)
f6.pack(side=TOP,fill=X)
l6=Label(f6,text='27-01-2022	Artificial intelligence',font='mango 35 bold',fg='cyan',bg='Black')
l6.pack()

f7=Frame(root,bg='Black',relief=SUNKEN,borderwidth=10)
f7.pack(side=TOP,fill=X)
l7=Label(f7,bg='Black',fg='lavender',text='01-02-2022	Science',font='mango 35 bold')
l7.pack()



f8=Frame(root,bg='Black',relief=SUNKEN,borderwidth=10)
f8.pack(side=BOTTOM,fill=X)
l8=Label(f8,bg="Yellow",fg="Dark green",font="mango 50 bold",text='Time =  11:30am to12:30pm',pady=1000)
l8.pack()





root.mainloop()







root.mainloop()