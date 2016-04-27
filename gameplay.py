from tkinter import *
import tkinter.messagebox

file = open("words.txt", "r")
words = file.readline().lower()
used_words = []
new_words = []
new = ""
num = 0


def generate_word_easy(word):
    gen_word = list(word)
    char = 'a'
    for i in range(0, 4):
        for j in range(0, 26):
            gen_word[i] = chr(ord(char) + j)
            new_word = ''.join(gen_word)
            # print(new_word)
            if new_word in words and new_word not in used_words:
                return new_word
        gen_word[i] = word[i]
    return "Word Doesn't Exist!"


def check_word_validity(word, num=num):
    if word in used_words:
        tkinter.messagebox.showwarning("Addictionary", "Word already used!")
        # print("Word is already used!")
        return False
    if word not in words:
        tkinter.messagebox.showwarning("Addictionary", "Word in not valid!")
        # print("Word is not a valid word!")
        return False
    if word == "Exit Game":
        return False
    return True


def check_new_word_validity(word, num=num):
    new = generate_word_easy(word)
    flag = 0
    while new != word:
        if new == word:
            flag = 1
            break
        new = generate_word_easy(word)
    if flag != 1:
        tkinter.messagebox.showwarning("Addictionary", "Invalid Word!")
        return False
    return True


def submit(num=num, new=new):
    word = new_word_entry.get()
    if check_word_validity(word):# and check_new_word_validity(word):
        new = generate_word_easy(word)
        used_words.append(word)
        used_words.append(new)
        comp = "Player : " + word
        Label(frame, text=comp).grid(row=num, column=0)
        num += 1
        comp = "Computer : " + new
        Label(frame, text=comp).grid(row=num, column=0)
        num += 1
        print(num)

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
