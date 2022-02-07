from tkinter import *
root=Tk()
root.geometry("655x333")

frame_1=Frame(root,background="Black",relief=RIDGE,borderwidth=1)
frame_1.pack(side=TOP,anchor='nw',fill=X)
lable_1=Label(frame_1,text="File    Edit    View    Navigate    Code    Run     Tools   VCS     Window      Help        "
                           "                                                                                            "
                           "                                                                                           - []  x "
                           "                 ",fg='white',background='black',font='mango 10 bold',padx=20)

frame_2=Frame(root,background="Black",relief=RIDGE,borderwidth=1)
frame_2.pack(side=TOP,anchor='nw',fill=X)
lable_2=Label(frame_2,text="tut 1.py  x  tut 2.py  x    tut 3.py  x    tut 4.py  x    tut 5.py  x    tut 6.py  x     tut 7.py  x   tut 8.py  x        "
                           "                                                                                                                          "
                           "                                                                                                                              "
                                    
                           "                 ",fg='white',background='black',font='mango 8 bold',padx=10)

frame_3=Frame(root,background="Black",relief=RIDGE,borderwidth=1)
frame_3.pack(side=TOP,anchor='nw',fill=Y)
lable_3=Label(frame_3,text="""1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
""",fg="white",bg="black",pady=800)



lable_3.pack()
lable_2.pack()
lable_1.pack()


root.mainloop()