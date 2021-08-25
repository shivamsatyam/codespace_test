from tkinter import *
from tkinter.ttk import *
from time import strftime
from tkinter import messagebox

root = Tk()
root.title("Clock")
root.wm_iconbitmap('clock.ico')
root.resizable(0,0)

def time():
	string = strftime('%H:%M:%S %p')
	label.config(text=string)
	label.after(1000, time)

label = Label(root, font=("DS-Digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')

time()

def message():
	if messagebox.askyesnocancel("Close", "Do you want to close?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",message)

root.mainloop()