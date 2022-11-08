# Import the required libraries
from tkinter import *
from tkinter import font
import tkinter as tk
# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Create two frames in the window
greet = Frame(win)
order = Frame(win)


def näita():
    INPUT = entry1.get("1.0","end-1c" )
    

# Define a function for switching the frames
def esilehele():
   greet.pack(fill='both', expand=1)
   order.pack_forget()

def sõnu_sisestama():
   order.pack(fill='both', expand=1)
   greet.pack_forget()

# Create fonts for making difference in the frame
font1 = font.Font(family='Georgia', size='12', weight='bold')
font2 = font.Font(family='Aerial', size='12')


label_text = "Saad valida kolme õppimismeetodi vahel.\n \
Esimene meetod annab sulle eestikeelse sõne ja sa pead selle tõlkima.\n \
Teine meetod annab sulle ette vöörkeelse sõna ja sa pead kirjutama sellele vaste. \n \
Kolmas meetod annab sulle ette sõna ning sa pead vastama kas tõlge on õige või vale."

# Add a heading logo in the frames
label1 = Label(greet, text=label_text, font=font1)
label1.pack(pady=20)

label2 = Label(order, text="Sisestage sõnad mida soovite õopida.", font=font2)
label2.pack(pady=20)

esilehele()

# Add a button to switch between two frames
btn1 = Button(greet, text="Sõnu sisestama", font=font2, command=sõnu_sisestama)
btn1.pack(pady=0)

btn2 = Button(order, text="Esilehele", font=font2, command=esilehele)
btn2.pack(pady=20)

#Sõnade sisestamise box
entry1 = tk.Text(order, height = 12, width = 20)
entry1.pack()

näita = Button(order, height = 2, width =20, text = "näita", command = näita)
näita.pack()

win.mainloop()