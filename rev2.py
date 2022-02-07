# """
# from tkinter import *
# root=Tk()
# root.geometry("500x300")
# root.title("Input GUI")
# def iii():
#     print(a_s.get())
# a=Label(root,text="Name ",fg="Black",font="mango 10 bold",padx=20)
# a.grid()
#
#
# a_s=StringVar()
#
#
# a_e=Entry(root,textvariable=a_s,font="mango 10 bold")
# a_e.grid(row=0,column=1)
#
# b_e=Button(text='Sumbit',command=iii,font="mango 10 bold").grid()
#
#
#
# if __name__ == '__main__':
#     root.mainloop()
# """
#
# from tkinter import*
# root=Tk()
#
#
# #Command¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢
#
# def com():
# 	if True :
# 		with open('User.txt','a') as f:
# 			f.write(f"""
# User name is {i1.get()}
# User Class is {i2.get()}
# User Roll no is {i3.get()}
# User School is {i4.get()}
# User number is {i5.get()}\n\n
# 			""")
#
#
# #@@@@@@@@@@@@@@@@@@@@@@
#
# label=Label(text="Welcome",font='mango 20 bold')
# label.grid(row=0,column=1)
#
# root.geometry("400x300")
# root.title("GUI")
#
# #@@@@@@@@@@@@@@@@@@@@@@
# f1=Frame(root,bg="Black",relief=SUNKEN,borderwidth=3)
# f1.grid()
# l1=Label(f1,text="  Name   ",fg='Black')
# l1.grid()
# i1=StringVar()
# e1=Entry(root,textvariable=i1)
# e1.grid(row=1,column=1)
# #################################
#
#
# f2=Frame(root,bg="Black",relief=SUNKEN,borderwidth=3)
# f2.grid()
# l2=Label(f2,text="   Class   ",fg='Black')
# l2.grid()
# i2=StringVar()
# e2=Entry(root,textvariable=i2)
# e2.grid(row=2,column=1)
# #################################
# f0=Frame(root,bg='Black',borderwidth=3,relief=SUNKEN)
# f0.grid()
# l0=Label(f0,text=' Section ',fg="Black")
# l0.grid()
# i0=StringVar()
# e0=Entry(root,textvariable=i0)
# e0.grid(row=3,column=1)
# ##################################
#
# f3=Frame(root,bg="Black",relief=SUNKEN,borderwidth=3)
# f3.grid()
# l3=Label(f3,text="  Roll no ",fg='Black')
# l3.grid()
# i3=StringVar()
# e3=Entry(root,textvariable=i3)
# e3.grid(row=4,column=1)
# #################################
# f4=Frame(root,bg="Black",relief=SUNKEN,borderwidth=3)
# f4.grid()
# l4=Label(f4,text="  School  ",fg='Black')
# l4.grid()
# i4=StringVar()
# e4=Entry(root,textvariable=i4)
# e4.grid(row=5,column=1)
# ##################################
# f5=Frame(root,bg="Black",relief=SUNKEN,borderwidth=3)
# f5.grid()
# l5=Label(f5,text=" Number",fg='Black')
# l5.grid()
# i5=StringVar()
# e5=Entry(root,textvariable=i5)
# e5.grid(row=6,column=1)
#
#
#
#
#
#
# #₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹
# b1=Button(root,text='Sumbit',font="mango 10 bold",command=com)
# b1.grid(column=1)
# b2=Button(root,text='Quit',font='mango 10 bold',command=quit)
# b2.grid(column=1)
# #₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹
#
#
# if __name__ == '__main__':
#     root.mainloop()




from tkinter import*
root=Tk()



l1=Label(text='G',fg='Blue',font='mango 150 bold')
l1.grid(row=1,column=1)

l2=Label(text='o',fg='Red',font='mango 150 bold')
l2.grid(row=1,column=2)

l3=Label(text='o',fg='Yellow',font='mango 150 bold')
l3.grid(row=1,column=3)

l4=Label(text='g',fg='Blue',font='mango 150 bold')
l4.grid(row=1,column=4)

l5=Label(text='l',fg='Green',font='mango 150 bold')
l5.grid(row=1,column=5)

l6=Label(text='e',fg='Red',font='mango 150 bold')
l6.grid(row=1,column=6)

l7=Label(text='T',fg='Black',font='mango 15 bold')
l7.grid(row=1,column=8)

l7=Label(text='M',fg='Black',font='mango 15 bold')
l7.grid(row=1,column=9)



fr=Frame(borderwidth=2,relief=SUNKEN)
fr.grid(row=3,column=3)
Fr=Frame(borderwidth=2,relief=SUNKEN)
Fr.grid(row=3,column=4)

B1=Button(fr,text="search",font='mango 20 bold')
B1.grid()

inp=StringVar()
en=Entry(root,textvariable=inp,font='mango 50 bold')
en.grid()

B2=Button(Fr,text='  quit ',font='mango 20 bold',padx=3,command=quit)
B2.grid(row=3,column=4)


root.mainloop()