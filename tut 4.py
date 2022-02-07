from tkinter import *

hardik_root=Tk()

# Width x Height
hardik_root.geometry("733x434")   # Screen size

# Width , Height
hardik_root.minsize(300,100)    # Limited small size

# Width , Height
hardik_root.maxsize(1200,600) # limited big size

abhishek = Label(text="Welcome to pycharm")
abhishek.pack()

hardik_root.mainloop()