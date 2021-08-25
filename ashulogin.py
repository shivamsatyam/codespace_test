from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login")
root.geometry("325x475")
root.wm_iconbitmap('login.ico')
root.resizable(0,0)

# Functions
def log():
		print("Thanks for login")
		print("The value of name=",namevalue.get())
		print("The value of phone=",phonevalue.get())
		print("The value of email=",emailvalue.get())
		print("The value of password=",passwordvalue.get())

		with open("ashulogin.txt", "a")as f:
			f.write(f"name = {namevalue.get()}\n phone = {phonevalue.get()}\n email = {emailvalue.get()}\n password = {passwordvalue.get()}\n")

			def clearvar():
				namevalue.set(" ")
				phonevalue.set(" ")
				emailvalue.set(" ")
				passwordvalue.set(" ")
				

			clearvar()
			root.destroy()

# Vars
namevalue = StringVar()
phonevalue = StringVar() 
emailvalue = StringVar()
passwordvalue = StringVar()

# Body structure
f = Frame(root, bg="black")

Label(f, text="Please Login", bg="black", fg="cyan", font="Ds-Digital 30",width=30).pack()
Label(f, text="-----------------", bg="black", fg="cyan", font="Ds-Digital 30").pack()

Label(f, text="Name", bg="black", fg="cyan", font="Ds-Digital 20").pack()
Entry(f, textvariable=namevalue, bg="white", fg="darkblue", width=15, font="Lucida 20").pack()

Label(f, text="Phone", bg="black", fg="cyan", font="Ds-Digital 20", pady=10).pack()
Entry(f, textvariable=phonevalue, bg="white", fg="darkblue", width=15, font="Lucida 20").pack(padx=5)

Label(f, text="E-mail", bg="black", fg="cyan", font="Ds-Digital 20", pady=10).pack()
Entry(f, textvariable=emailvalue, bg="white", fg="darkblue", width=15, font="Lucida 20").pack()

Label(f, text="Password", bg="black", fg="cyan", font="Ds-Digital 20", pady=10).pack()
Entry(f, textvariable=passwordvalue, bg="white", fg="darkblue", width=15, font="Lucida 20").pack()

Button(f, text="Login", bg="black", fg="cyan", activeforeground="cyan", activebackground="black", font="Ds-Digital 20", command=log).pack(pady=10)

f.pack()

# Message after cut button
def message():
	if messagebox.askyesnocancel("Close", "Do you want to close?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",message)

root.mainloop()