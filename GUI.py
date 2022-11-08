# Import the library
from tkinter import *
from tkinter import filedialog

# Create an instance of window
win=Tk()

# Set the geometry of the window
win.geometry("700x350")

# Create a frame widget
frame=Frame(win, width=300, height=300)
frame.grid(row=0, column=0, sticky="NW")

# Create a label widget
label=Label(win, text="", font='Arial 17 bold')
label.place(relx=0.5, rely=0.5, anchor=CENTER)

win.mainloop()