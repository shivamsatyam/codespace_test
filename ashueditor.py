from tkinter import *
from tkinter import messagebox,filedialog

root = Tk()
root.geometry("1280x850")
root.resizable(0,0)
root.title("Textpad")
root.wm_iconbitmap('editor.ico')

def open1():
	global file
	# if file:
	# 	messagebox.askyesnocancel(file,"Do you want to save file")
	try:

		file = filedialog.askopenfilename(filetypes=[("text document",".txt")])#("All files","*.*"),
		with open(file,"r") as op:
			text.delete(1.0,END)
			text.insert(1.0,op.read())
		root.title(os.path.basename(file))	
	except Exception as r:
		pass	

def save():
		file = filedialog.asksaveasfile(defaultextension='.txt',
										filetypes=[
											("Text file",".txt"),
											("All files","*.*"),
											("HTML files",".html")])
		filetext = str(text.get(1.0,END))
		file.write(filetext)
		file.close()

f = Frame(root)

Label(f, text="Select your file", fg="red", font="Ds-Digital 40 bold").pack()
Button(f, text="Select", bg="gray", fg="white", width=20, command=open1, font="20").pack(side=LEFT, padx=10)
Button(f, text="Save", bg="gray", fg="white", width=20, command=save, font="20").pack(side=LEFT, padx=10)

f.pack()


text = Text(root,font="arial 25",undo=True)
text.pack(expand=True,fill=BOTH,padx=12)
def exit_func(event=None):
	global file, text_changed
	try:
		if text_changed:
			mbox = messagebox.askyesnocancel("warning", "do you want to save it")
			
			if mbox is True:
				if file:
					with open(file,"w") as op:
						op.write(str(text.get(1.0,END)))
						root.destroy()
				else:

					file = filedialog.asksaveasfile(mode="w",initialdir=os.getcwd(),defaultextension=".txt",
													filetypes=[
														("Text document as",".txt"),
														("All files","*.*")									
													])	
					filetext = str(text.get(1.0,END))
					file.write(filetext)
					file.close()
			else:
				root.destroy()	
	except Exception as w:
		pass
scroll = Scrollbar(text)
scroll.pack(side=RIGHT,fill=Y)
text.config(yscrollcommand=scroll.set)
scroll.config(command=text.yview)

def message():
	if messagebox.askyesnocancel("Close", "Do you want to close?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",message)


root.mainloop()