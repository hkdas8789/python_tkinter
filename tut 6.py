from tkinter import*

root=Tk()


root.geometry("400x500")
root.minsize(300,400)
# root.maxsize(500,700)
root.wm_title('IGI')
label=Label(text='Play IGI 2\nMultiplayer\nConfiguration\nSelect Player\nCredits\nQuit ',
            background='dark blue',     # text boundry
            fg='light blue',    # text color
            padx=50,
            pady=50,
            font=("comicsansms", 19,'bold'),    # font 1. string 2. 3.text size --> bold
            borderwidth=10, # boder bouundry
            relief=RIDGE # boder stile totle stile --> SUNKEN, RAISED, GROOVE, RIDGE
            )

# Importent pack options
# anchor=nw
# side = TOP,BOTTOM,LEFT,RIGHT
# fill
# padx
# pady

label.pack(
side=BOTTOM,
anchor='n'  , # You can arange the text in "nw" is 'northwest' and only "ne" 'northeast' direction.
fill=X   ,# increase size
padx=30,
 pady=40
           )



root.mainloop()






