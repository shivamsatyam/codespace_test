from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Convertor")
root.geometry("1280x720")
root.resizable(0,0)
root.wm_iconbitmap("convertor.ico")

def convert():
	if num.get()==0:
		messagebox.showerror('Error','Please write number')
	else:
		binary.set(str(bin(num.get())))
		decimal.set(str(num.get()))
		hexa.set(str(hex(num.get())))
		octal.set(str(oct(num.get())))

def reset():
	num.set(0)
	binary.set("")
	decimal.set("")
	hexa.set("")
	octal.set("")

Label(root, text="Conversion System", bg="black", fg="cyan", font=" Ds-Digital 45 bold").pack(padx=10)

num = IntVar()
binary = StringVar()
decimal = StringVar()
hexa = StringVar()
octal = StringVar()

Label(root, text="Enter number", bg="black", fg="cyan", font="Ds-Digital 25").place(x=340, y=150)
Label(root, text="Binary", bg="black", fg="cyan", font="Ds-Digital 25").place(x=340, y=230)
Label(root, text="Decimal", bg="black", fg="cyan", font="Ds-Digital 25").place(x=340, y=310)
Label(root, text="Hexa decimal", bg="black", fg="cyan", font="Ds-Digital 25").place(x=340, y=390)
Label(root, text="Octal", bg="black", fg="cyan", font="Ds-Digital 25").place(x=340, y=470)

Entry(root, textvariable=num, font="arial 25", bg="black", fg="cyan", justify=CENTER).place(x=600, y=150)
Entry(root, textvariable=binary, font="arial 25", bg="black", fg="cyan", justify=CENTER).place(x=600, y=230)
Entry(root, textvariable=decimal, font="arial 25", bg="black", fg="cyan", justify=CENTER).place(x=600, y=310)
Entry(root, textvariable=hexa, font="arial 25", bg="black", fg="cyan", justify=CENTER).place(x=600, y=390)
Entry(root, textvariable=octal, font="arial 25", bg="black", fg="cyan", justify=CENTER).place(x=600, y=470)

Button(root, text="Convert", bg="black", fg="cyan", font="Ds-Digital 25", command=convert).place(x=550, y=600)
Button(root, text="Reset", bg="black", fg="cyan", font="Ds-Digital 25", command=reset).place(x=900, y=600)

def message():
	if messagebox.askyesnocancel("Close", "Do you want to close?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",message)

root.mainloop()