#!/usr/bin/env python3
import os 
from Tkinter import *

python = 'c:\Python27-x64\python'

class Application (Frame):

	found = False
	def __init__(self, master):
		# Initialize the Frame
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()
		self.run_tcpdstat()

	def create_widgets(self):
		# create hash buttons 
		self.title = Label(self, text= "WELCOME TO THE DFC")

		self.title.grid()
		self.thelabel = Label(self, text = "Press to Hash Folder")
		self.thelabel.grid()  
		self.submit_button=Button(self, command = lambda: self.change_bool(), text = "Hash")
		self.submit_button.grid()

	def change_bool(self):
		self.found = True
		self.import_file()



	rootdir = '/Users/MikeO/Desktop/Hasher/' # Dir path
        lindir = '/home/beast/hash' # Linux dir 
        windir = 'C:\\Users\\timbooks\\Desktop\\HasherTestArea' # Dir path on a windows machine
        
        hashFileName = 'HashedStuff'
	directoryToHash = windir

	def import_file(self):
		if (self.found):
			os.system(python + 'hash.py' + hashFileName + ' ' + directoryToHash)	

	def run_tcpdstat(self):
		self.instruction = Label(self, text= "Enter file location")
		self.instruction.grid(row= 3, column = 1, columnspan = 2, sticky = W)

		self.password = Entry(self)
		self.password.grid(row =4, column = 1, sticky = W)


		self.submit = Button(self, text="Submit", command = self.reveal)
		self.submit.grid(row= 5, column = 0, stick = W)

		self.text = Text(self, width = 35, height = 5, wrap = WORD)
		self.text.grid(row =6, column =0, columnspan= 2, sticky = W)

	def reveal(self):
		content = self.password.get()
		tcpdstat= "tcpdstat -c 100 "+ content
		f = os.popen(tcpdstat)
		message = f.read()
		print message
		print tcpdstat
		self.text.delete(0.0, END)
		self.text.insert(0.0, message)


		
root = Tk()
root.title("DFC Tool")
root.geometry("500x400")

app = Application(root)
root.mainloop()
