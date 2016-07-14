from Tkinter import *
root = Tk()
tile1 = Label(root, text = "Hello GUI world  :)")
tile1.pack(side=TOP, expand=YES, fill=BOTH)

def hello(event):
	print "Press twice to exit.."

def quit(event):
	print "Bye bye"
	sys.exit()

def close():
	print "Quitting"
	sys.exit()

tile2 = Button(root, text='Close Window', command=close)
tile2.pack(side=BOTTOM)

tile3 = Button(root, text = "Event hanlder button")
tile3.pack(side=LEFT)
tile3.bind('<Button-1>',hello)
tile3.bind('<Double-1>',quit)

root.title('My window')
root.mainloop()