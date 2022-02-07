# from tkinter import *
# root=Tk()
# Width=400
# Height=200
# root.geometry(f"{Width}x{Height}")
# canvas=Canvas(width=Width,height=Height,bg="Blue")
# canvas.grid()
#
# """Create line with coordinates x1,y1,...,xn,yn."""
# # canvas.create_line(0,200,400,0,width=10,fill="red")
# # canvas.create_rectangle(50,30,200,100,width=10)
# # canvas.create_text(200,200,text="Welcome")
# canvas.create_oval(100,200,200,100,width=10,fill="green")
#
#
# if __name__=='__main__':
#     root.mainloop()
from tkinter import *


root = Tk()

C = Canvas(root, bg="yellow",
		height=250, width=300)

line = C.create_line(108, 120,
					320, 40,
					fill="green")

arc = C.create_arc(180, 150, 80,
				210, start=0,
				extent=220,
				fill="red")

oval = C.create_oval(80, 30, 140,
					150,
					fill="blue")

C.pack()
mainloop()
