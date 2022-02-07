# # from tkinter import *
# # root = Tk()
# #
# # i = IntVar()
# # a = Checkbutton(text="Want to prebook your meals?",variable = i).grid()
# # root.mainloop()
#
#
# from tkinter import*
# from PIL import Image ,ImageTk
# root=Tk()
# root.geometry("500x200")
# root.minsize(100,100)
# root.title("Revision")
# def value():
#     print(f"The name is {i_1.get()}")
#     print(f"The gender is {i_2.get()}")
#     print(f"The phone number is {i_3.get()}")
#
# '''i=IntVar()
# Checkbutton().grid()'''
#
#
# # Image IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
#
# im=Image.open("tiger.PNG")
# ds=ImageTk.PhotoImage(im)
# li=Label(image=ds).grid(row=2,column=6)
#
#
#
#
#
#
# main_Frame1=Frame(root,bg="Cyan",borderwidth=10 ,relief=SUNKEN)
# main_Frame1.grid(row=0,column=4)
#
# main_Frame=Frame(root,bg="Black",borderwidth=10,relief=SUNKEN)
# main_Frame.grid(row=1,column=1,pady=30)
# l0=Label(text="Welcome to abhishek travels",font="mango 20 bold",bg="Cyan",padx=50).grid(row=0,column=4)
#
#
# l1=Label(main_Frame,text="Name",font="mango 15 bold",bg="Black",padx=29,fg="Cyan").grid(row=1,column=1)
# l2=Label(main_Frame,text="Gender",font="mango 15 bold",bg="Black",padx=24,fg="Cyan").grid(row=2,column=1)
# l3=Label(main_Frame,text="Phone number",font="mango 15 bold",bg="Black",fg="Cyan").grid(row=3,column=1)
#
# i_1=StringVar()
# i_2=StringVar()
# i_3=StringVar()
# _1=IntVar()
#
#
# e1=Entry(main_Frame,textvariable=i_1,font="mango 15 bold",).grid(row=1,column=2)
# e2=Entry(main_Frame,textvariable=i_2,font="mango 15 bold",).grid(row=2,column=2)
# e3=Entry(main_Frame,textvariable=i_3,font="mango 15 bold",).grid(row=3,column=2)
#
# Button(main_Frame,text="Submit",font="mango 10 bold",command=value).grid(row=5,column=2,pady=10)
# Checkbutton(main_Frame,text="Are all right?",variable=_1,bg="Black",fg="Cyan",font="mango 10 bold").grid(row=5,column=1)
#
#
#
#
# root.mainloop()


from tkinter import*
root=Tk()

width=243
height=213

root.geometry(f"{width}x{height}")
root.minsize(width,height)
root.maxsize(width,height)

root.title("GUI")

def value():
	print(f"User name is {i1.get()},")
	print(f"Class is {i2.get()},")
	print(f"Section is {i3.get()},")
	print(f"School name is {i4.get()},")
	print(f"Phone number is {i5.get()}\n\n")
	f=open("User11111111111111111111111111111111111111111111111111.txt","a")
	f.write(f'User name is {i1.get()},\nClass is {i2.get()},\nSection is {i3.get()},\n School name is {i4.get()},\nPhone number is {i5.get()}.\n\n')
	f.close()



F1=Frame(root,bg='Black',borderwidth=7,relief=SUNKEN)
F1.grid()



L0=Label(F1,text='Welcome',bg="Black",fg="Cyan",font='mango 15 bold',pady=10)
L0.grid(row=0,column=2)



L1=Label(F1,text='Name',font='mango 10 bold',bg='Black',fg='Cyan',padx=10)
L1.grid(row=1,column=1)

# Fix size

L2=Label(F1,text='Class',font='mango 10 bold',bg='Black',fg='Cyan',padx=10)
L2.grid(row=2,column=1)


L3=Label(F1,text=' Sec ',font='mango 10 bold',bg='Black',fg='cyan',padx=10)
L3.grid(row=3,column=1)



L4=Label(F1,text='School',font='mango 10 bold',bg='Black',fg='Cyan',padx=10)
L4.grid(row=4,column=1)




L5=Label(F1,text='Phone no',font='mango 10 bold',bg='Black',fg='Cyan',padx=10)
L5.grid(row=5,column=1)




i1=StringVar()
i2=StringVar()
i3=StringVar()
i4=StringVar()
i5=StringVar()
Intv1=IntVar()





e1=Entry(F1,textvariable=i1,font='mango 10 bold')
e1.grid(row=1,column=2)


e2=Entry(F1,textvariable=i2,font='mango 10 bold')
e2.grid(row=2,column=2)



e3=Entry(F1,textvariable=i3,font='mango 10 bold')
e3.grid(row=3,column=2)



e4=Entry(F1,textvariable=i4,font='mango 10 bold')
e4.grid(row=4,column=2)




e5=Entry(F1,textvariable=i5,font='mango 10 bold')
e5.grid(row=5,column=2)





F2=Frame(bg='Black',borderwidth=7,relief=SUNKEN)
F2.grid(row=5)


Button(F2,text='Submit',font="mango 10 bold",command=value,padx=5).grid(row=4,column=2)


Button(F2,text='quit',font='mango 10 bold',command=quit,padx=5).grid(row=4,column=1)









Checkbutton(F2,text="Are all right?",font='mango 10 bold',pady=2,command=Intv1,padx=5).grid(row=4,column=3)













root.mainloop()
