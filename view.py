from tkinter import *

myapp = Tk()

def new():
    top = Toplevel()
    print("new")


myapp.wm_title("Addictionary")
myapp.geometry("500x500")
myapp.resizable(0, 0)
myapp.config(background="#28ABE3")

menubar = Menu(myapp)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Game", command=new)
filemenu.add_separator()
filemenu.add_command(label="Close", command=myapp.quit)
menubar.add_cascade(label="Game", menu=filemenu)
myapp.config(menu=menubar)

filename1 = PhotoImage(file="res/logo.png", width="361", height="71")
logo = Label(myapp, image=filename1, bg="#28ABE3")
logo.pack()

new_btn = Button(myapp, relief=FLAT, bg="#28ABE3")
filename2 = PhotoImage(file="res/new_game.png")
new_btn.config(image=filename2, width="183", height="43")
new_btn.pack()

rul_btn = Button(myapp, relief=FLAT, bg="#28ABE3")
filename3 = PhotoImage(file="res/rules.png")
rul_btn.config(image=filename3, width="101", height="43")
rul_btn.pack()

myapp.mainloop()
