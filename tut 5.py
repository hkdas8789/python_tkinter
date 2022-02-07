from PIL import Image,ImageTk

from tkinter import *

kuhu=Tk()




kuhu.geometry("400x300")
kuhu.minsize(200,100)
# kuhu.maxsize(500,400)

photo=ImageTk.PhotoImage(file="2.jpg.png")
show = Label(image=photo)
show.pack()

kuhu.mainloop()