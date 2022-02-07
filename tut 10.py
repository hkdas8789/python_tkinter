from tkinter import *
root=Tk()
root.geometry("655x333")

def getvals():
    print(u_v.get())
    print(p_v.get())

##################################
u=Label(root,text="User name")
p=Label(root,text="Password")
u.grid()
p.grid()
##################################
u_v=StringVar()
p_v=StringVar()
###############
u_e=Entry(root,textvariable=u_v)
p_e=Entry(root,textvariable=p_v)
u_e.grid(row=0,column=1)
p_e.grid(row=1,column=1)
##################################
Button(text="sumbit",command=getvals).grid()

if __name__ == '__main__':
    root.mainloop()