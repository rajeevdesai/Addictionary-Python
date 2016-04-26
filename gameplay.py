from tkinter import *

root = Tk()

root.wm_title("Addictionary")
root.geometry("400x400")
# root.resizable(0, 0)
root.config(background="#28ABE3")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Game")
filemenu.add_separator()
filemenu.add_command(label="Close", command=root.quit)
menubar.add_cascade(label="Game", menu=filemenu)
root.config(menu=menubar)

filename = PhotoImage(file="res/logo.png", width="361", height="71")
logo = Label(root, image=filename, bg="#28ABE3")
logo.pack(side=TOP)

new_word_frame = Frame(root, bg="#28ABE3")
new_word_frame.pack(side=BOTTOM)

new_word_label = Label(new_word_frame, text="Enter Word:", height=3, font=12, bg="#28ABE3", fg="#313130")
new_word_label.pack(side=LEFT)

new_word_entry = Entry(new_word_frame, font=12, bg="#ECDFBD")
new_word_entry.pack(side=LEFT)


def submit():
    Label(frame, text=new_word_entry.get()).grid(row=1,column=0)

new_word_button = Button(new_word_frame, text="Submit", font=10, bg="#1FDA9A", fg="#313130", command=submit)
new_word_button.pack(side=RIGHT)


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=300, height=275)


myframe = Frame(root, width=65, height=100, bd=1)
myframe.pack()

canvas = Canvas(myframe, bg="#ECDFBD")
frame = Frame(canvas)
myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right", fill="y")
canvas.pack(side="left")
canvas.create_window((0, 0), window=frame, anchor='nw')
frame.bind("<Configure>", myfunction)

root.mainloop()
