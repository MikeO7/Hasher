#!/usr/bin/env python3
import os 
from Tkinter import *
import tkFileDialog

python = 'c:\Python27-x64\python'

class Application (Frame):
		
	rootdir = '/Users/MikeO/Desktop/Hasher/' # Dir path
	lindir = '/home/beast/hash' # Linux dir 
	windir = 'C:\\Users\\timbooks\\Desktop\\HasherTestArea' # Dir path on a windows machine
	   
	hashFileName = 'HashedStuff'
	directoryToHash = windir
	
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

		self.title.grid(row=0, column=0)
		self.thelabel = Label(self, text = "Press to Hash Folder")
		self.thelabel.grid(row=1, column=0)  
		self.submit_button=Button(self, command = lambda: self.change_bool(), text = "Hash")
		self.submit_button.grid(row=2, column=0)
		self.submit_button2=Button(self, command = lambda: self.get_file(), text = "Get File")
		self.submit_button2.grid(row=2, column=1)
		self.submit_button3=Button(self, command = lambda: self.get_directory(), text = "Get Directory to hash")
		self.submit_button3.grid(row=3, column=0)
		self.DirectoryLabel = Label(self, text = "The Directory which will be hashed: ")
		self.DirectoryLabel.grid(row=4, column=0) 
		self.DirectoryLabel = Label(self, text = self.directoryToHash)
		self.DirectoryLabel.grid(row=5, column=0) 
		

	def change_bool(self):
		self.found = True
		self.import_file()

		
	def get_file(self):
		self.found = True
		self.f = (tkFileDialog.askopenfilename(parent=root))
		print self.f

		
	def get_directory(self):
		self.found = True
		self.d = (tkFileDialog.askdirectory(parent=root))
		print self.d
		self.directoryToHash = self.d
		self.DirectoryLabel = Label(self, text = self.directoryToHash)
		self.DirectoryLabel.grid(row=5, column=0) 

	def import_file(self):
		print self.hashFileName
		print self.directoryToHash
		if (self.found):
			os.system(python + ' hash.py "' + self.hashFileName + '" "' + self.directoryToHash +'"')    

	def run_tcpdstat(self):
		self.instruction = Label(self, text= "Enter file location")
		self.instruction.grid(row= 3, column = 1, columnspan = 2, sticky = W)

		self.password = Entry(self)
		self.password.grid(row =4, column = 1, sticky = W)


		self.submit = Button(self, text="Submit", command = self.reveal)
		self.submit.grid(row= 6, column = 0, stick = W)

		self.text = Text(self, width = 35, height = 5, wrap = WORD)
		self.text.grid(row =7, column =0, columnspan= 2, sticky = W)

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
