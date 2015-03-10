#!/usr/bin/env python3
import os 
from Tkinter import *
from ttk import *
import tkFileDialog

python = 'c:\Python27-x64\python'

class Application (Frame):
		
	rootdir = '/Users/MikeO/Desktop/Hasher/' # Dir path
	lindir = '/home/beast/hash' # Linux dir 
	windir = 'C:\\Users\\timbooks\\Desktop\\HasherTestArea' # Dir path on a windows machine
	   
	hashFileName = 'HashedStuffHERE'
	directoryToHash = windir

	
	found = False
	def __init__(self, master):
		# Initialize the Frame
		Frame.__init__(self,master)
		self.note = Notebook(self.master)
		self.tab1 = Frame(self.note)
		self.tab2 = Frame(self.note)
		self.tab3 = Frame(self.note)
		#Button(tab1, text='Exit', command=root.destroy).pack(padx=100, pady=100)

		self.note.add(self.tab1, text = "Hasher")
		self.note.add(self.tab2, text = "TcpdStat")
		self.note.add(self.tab3, text = "Tab Three")
##		self.create_tab1()
		
		self.note.pack()
		
#		self.grid()
		self.create_widgets()
		self.run_tcpdstat()
		
		
	def create_tab1(self):
		# fill tab1
		self.exitButton = Button(self.tab1, text='Exit', command=root.destroy).pack(padx=100, pady=100)
		

	def create_widgets(self):
		# create hash buttons 
		self.title = Label(self.tab1, text= "WELCOME TO THE DFC")

		self.title.grid(row=0, column=0)
		self.thelabel = Label(self.tab1, text = "Press to Hash Folder")
		self.thelabel.grid(row=1, column=0)  
		self.submit_button=Button(self.tab1, command = lambda: self.change_bool(), text = "Hash")
		self.submit_button.grid(row=2, column=0)
		self.submit_button3=Button(self.tab1, command = lambda: self.get_directory(), text = "Get Directory to hash")
		self.submit_button3.grid(row=3, column=0)
		self.DirectoryLabel = Label(self.tab1, text = "The Directory which will be hashed: ")
		self.DirectoryLabel.grid(row=4, column=0, columnspan = 2) 
		self.DirectoryLabel = Label(self.tab1, text = self.directoryToHash)
		self.DirectoryLabel.grid(row=5, column=0, columnspan=2) 
		

	def change_bool(self):
		self.found = True
		self.import_file()

		
	def get_file(self):
		self.found = True
		self.f = (tkFileDialog.askopenfilename(parent=root))
		print self.f
		self.password.delete(0, END)
		self.password.insert(0, self.f)
		

		
	def get_directory(self):
		self.found = True
		self.d = (tkFileDialog.askdirectory(parent=root))
		print self.d
		self.directoryToHash = self.d
		self.DirectoryLabel = Label(self.tab1, text = self.directoryToHash)
		self.DirectoryLabel.grid(row=5, column=0, columnspan=2) 

	def import_file(self):
		print self.hashFileName
		print self.directoryToHash
		if (self.found):
			os.system(python + ' hash.py "' + self.hashFileName + '" "' + self.directoryToHash +'"')    

	def run_tcpdstat(self):
		self.submit_button2=Button(self.tab2, command = lambda: self.get_file(), text = "Get File")
		self.submit_button2.grid(row=12, column=0)
		self.instruction = Label(self.tab2, text= "Enter file location")
		self.instruction.grid(row= 11, column = 1, columnspan = 2, sticky = W)

		self.password = Entry(self.tab2)
		self.password.grid(row =12, column = 1, sticky = W)


		self.submit = Button(self.tab2, text="Submit", command = self.reveal)
		self.submit.grid(row= 14, column = 0, stick = W)

		self.text = Text(self.tab2, width = 35, height = 5, wrap = WORD)
		self.text.grid(row =15, column =0, columnspan= 2, sticky = W)

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

##note = Notebook(root)
##tab1 = Frame(note)
##tab2 = Frame(note)
##tab3 = Frame(note)
##Button(tab1, text='Exit', command=root.destroy).pack(padx=100, pady=100)
##
##note.add(tab1, text = "Tab One")
##note.add(tab2, text = "Tab Two")
##note.add(tab3, text = "Tab Three")
##note.pack()

app = Application(root)
root.mainloop()
