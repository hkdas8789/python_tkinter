from tkinter import*
from PIL import Image ,ImageTk
root=Tk()
root.geometry('500x400')


im=Image.open('bird.jpg')
sh=ImageTk.PhotoImage(im)
la=Label(image=sh).pack(anchor='ne')
tx=Label(text='GUI is the best').pack(side='left',anchor='nw')




root.mainloop()