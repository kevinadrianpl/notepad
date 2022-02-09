import tkinter
import os	
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:

	__root = Tk()

	# Default windows width and height
	__thisWidth = 800
	__thisHeight = 600
	__thisTextArea = Text(__root)
	__thisMenuBar = Menu(__root)
	__thisFileMenu = Menu(__thisMenuBar, tearoff=0)
	__thisEditMenu = Menu(__thisMenuBar, tearoff=0)
	__thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
	
	# Add the scrollbar
	__thisScrollBar = Scrollbar(__thisTextArea)	
	__file = None

	def __init__(self,**kwargs):

		# Set the icon
		try:
				self.__root.wm_iconbitmap("/notes.ico")
		except:
				pass

		# Set window size (the default is 800x600)

		try:
			self.__thisWidth = kwargs['width']
		except KeyError:
			pass

		try:
			self.__thisHeight = kwargs['height']
		except KeyError:
			pass

		# Set the window text
		self.__root.title("Untitled - Basic Notepad")

		# Center the window
		screenWidth = self.__root.winfo_screenwidth()
		screenHeight = self.__root.winfo_screenheight()
	
		# For left-alling
		left = (screenWidth / 2) - (self.__thisWidth / 2)
		
		# For right-allign
		top = (screenHeight / 2) - (self.__thisHeight /2)
		
		# Top and bottom
		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
											self.__thisHeight,
											left, top))

		# Make the textarea auto resizable
		self.__root.grid_rowconfigure(0, weight=1)
		self.__root.grid_columnconfigure(0, weight=1)

		# Add controls (widget)
		self.__thisTextArea.grid(sticky = N + E + S + W)
		
		# Oopen a new file
		self.__thisFileMenu.add_command(label="New",
										command=self.__newFile)	
		
		# Open an existing .txt file
		self.__thisFileMenu.add_command(label="Open",
										command=self.__openFile)
		
		# Save the current file
		self.__thisFileMenu.add_command(label="Save",
										command=self.__saveFile)	

		# Create a line in the dialog		
		self.__thisFileMenu.add_separator()										
		self.__thisFileMenu.add_command(label="Exit",
										command=self.__quitApplication)
		self.__thisMenuBar.add_cascade(label="File",
									menu=self.__thisFileMenu)	
		
		# Cut feature
		self.__thisEditMenu.add_command(label="Cut",
										command=self.__cut)			
	
		# Copy feature
		self.__thisEditMenu.add_command(label="Copy",
										command=self.__copy)		
		
		# Paste feature
		self.__thisEditMenu.add_command(label="Paste",
										command=self.__paste)		
		
		# Editing feature
		self.__thisMenuBar.add_cascade(label="Edit",
									menu=self.__thisEditMenu)	
		
		# Create a feature to show the description of the notepad
		self.__thisHelpMenu.add_command(label="About",
										command=self.__showAbout)
		self.__thisMenuBar.add_cascade(label="Help",
									menu=self.__thisHelpMenu)

		self.__root.config(menu=self.__thisMenuBar)

		self.__thisScrollBar.pack(side=RIGHT,fill=Y)					
		
		# The scrollbar will adjust according to the content		
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)	
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
	
		
	def __quitApplication(self):
		self.__root.destroy()
		# exit()

	def __showAbout(self):
		showinfo("Basc Notepad","This is a basic note taking application made as a beginner friendly project.")

	def __openFile(self):
		
		self.__file = askopenfilename(defaultextension=".txt",
									filetypes=[("All Files","*.*"),
										("Text Documents","*.txt")])

		if self.__file == "":
			
			# No file selected to open
			self.__file = None
		else:
			
			# Open the file
			# Set the window title
			self.__root.title(os.path.basename(self.__file) + " - Basic Notepad")
			self.__thisTextArea.delete(1.0,END)

			file = open(self.__file,"r")

			self.__thisTextArea.insert(1.0,file.read())

			file.close()

		
	def __newFile(self):
		self.__root.title("Untitled - Basic Notepad")
		self.__file = None
		self.__thisTextArea.delete(1.0,END)

	def __saveFile(self):

		if self.__file == None:
			# Save as a new file
			self.__file = asksaveasfilename(initialfile='Untitled.txt',
											defaultextension=".txt",
											filetypes=[("All Files","*.*"),
												("Text Documents","*.txt")])

			if self.__file == "":
				self.__file = None
			else:
				
				# Save the file
				file = open(self.__file,"w")
				file.write(self.__thisTextArea.get(1.0,END))
				file.close()
				
				# Change the window title
				self.__root.title(os.path.basename(self.__file) + " - Basic Notepad")
				
			
		else:
			file = open(self.__file,"w")
			file.write(self.__thisTextArea.get(1.0,END))
			file.close()

	def __cut(self):
		self.__thisTextArea.event_generate("<<Cut>>")

	def __copy(self):
		self.__thisTextArea.event_generate("<<Copy>>")

	def __paste(self):
		self.__thisTextArea.event_generate("<<Paste>>")

	def run(self):

		# Main application
		self.__root.mainloop()


# Main application
notepad = Notepad(width=800,height=600)
notepad.run()
