#   pip install pywin32


def speak(string):
    from win32com.client import Dispatch
    Dispatch("SAPI.SpVoice").Speak(string)
if __name__ == '__main__':
    def calculate():
        try:
            from time import sleep
            speak("Enter your 1st number")
            n1=float(input("Enter your 1st number\n:-"))
            speak("Enter your 2nd number")
            n2=float(input("Enter your 2nd number\n:-"))
            p_s=f"The multipal of {n1} & {n2} is {n1*n2}"
            speak(p_s)
            print(p_s)
        except Exception as e:
            speak(e)
            print(e)
            sleep(1)
        finally:
            speak("Thank you,Bye")
            print("\n\n\t\t\tThank you\n\t\t\t\tBye\n\n\t\t\t")


def happy(year):
    try:
        from random import randint, choice
        from time import sleep

        while True:
            a = randint(10, 160)
            k = randint(2, 20)
            f = ["    ", "    ", "   ", f"Happy new year {year}", "    ", "    "]
            c = choice(f)
            print("  "*k, c, "  " * a, "*")

            #		print(c)
            sleep(0.2)


    except Exception as e:
        print(e)


# happy(2023)

from tkinter import *

root = Tk()
root.geometry("500x250")
root.title("Dance Form")

f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN, padx=23, pady=46)
f1.pack()

Label(f1, text="Dance Academy Form", font="helvetica 20 bold underline", pady=4, padx=25, fg="grey",
      bg="black", relief=SUNKEN).grid(column=1)




root.mainloop()











'''from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<>"))

def copy():
    TextArea.event_generate(("<>"))

def paste():
    TextArea.event_generate(("<>"))

def about():
    showinfo("Notepad", "Notepad by Code With Harry")

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("1.png")
    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file

    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    #Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()'''
