from Tkinter import *
root = Tk()

labelfont = ('times', 20, 'bold', 'italic')

widget = Label(root, text='Hello appearance world')
widget.config(bg='black', fg='yellow')
widget.config(font= labelfont)
widget.config(height=5, width=20) #initial size: lines, chars
widget.pack(expand=YES, fill=BOTH)
#root.config(bg='blue')
root.mainloop()