# Importing necessary libraries
from tkinter import *
from tkinter import messagebox

# Creating functions 
def confirm():
    password = entry1.get()
    passwordlen = len(password)
    if passwordlen <= 5:
        lbl2.config(text="Weak Password", fg="red")
    elif passwordlen >= 6 and passwordlen <= 8:
        lbl2.config(text="Medium Strong Password", fg="yellow")
    elif passwordlen > 8 and passwordlen <= 12:
        lbl2.config(text="Strong Password", fg="green2")
    else:
        lbl2.config(text="Very Strong Password", fg="dark green")

# Setting up the root
root = Tk()
root.geometry("500x400")
root.title("Password strength checker app")
root.configure(bg="turquoise1")

# Adding widgets to the screen
frame1 = Frame(root, bg="lawn green", height=200, width=300)
lbl1 = Label(frame1, text="Password:", font=('Brittanic Bold', 15), bg="DarkGoldenrod1")
entry1 = Entry(frame1, show="*")
lbl2 = Label(root, font=("Sitka Banner", 15), bg="turquoise1")
btn1 = Button(frame1, text="Confirm", command=confirm, bg="orange red", fg="white")
frame1.place(x=100, y=20)
lbl1.place(x=100, y=20)
entry1.place(x=88, y=80)
lbl2.place(relx=0.5, rely=0.7, anchor="center")
btn1.place(x=120, rely=0.7)

root.mainloop()