from tkinter import *
from tkinter import font
import tkinter as tk
import os


win = Tk()

win.geometry("700x350")

greet = Frame(win)
order = Frame(win)
meetod1f = Frame(win)
meetod2f = Frame(win)
meetod3f = Frame(win)

lista = []
listb = []
punktid = {}
rn=1

fail = open("sõnad.txt", "r")
data = fail.read()
count = 0
for line in fail:
    if count % 2 == 0:
        lista.append(line.strip())
        count +=1
    elif count % 2 != 0:
        listb.append(line.strip())
        count +=1

def näita():
    global lista
    global listb
    fail = open("sõnad.txt", "w")
    INPUT = entry1.get("1.0","end-1c" )
    count = 0
    INPUT = INPUT.split("\n")
    for line in INPUT:
        if line != "":
            fail.write(line + "\n")
        if count % 2 == 0:
            lista.append(line.strip())
            count +=1
        elif count % 2 != 0:
            listb.append(line.strip())
            count +=1
    if "" in lista:
        lista.remove("")
    if "" in listb:   
        listb.remove("")    
    for n in lista:
        punktid.update({n:0})
    fail.close()

def esilehele():
    greet.pack(fill='both', expand=1)
    order.pack_forget()
    meetod1f.pack_forget()
    meetod2f.pack_forget()
    meetod3f.pack_forget()

def sõnu_sisestama():
    order.pack(fill='both', expand=1)
    greet.pack_forget()

#MEETOD 1
def comp_s(event):
    print(lista)
    print(listb)
    try:
        global rn
        sisend = str(r.get())
        if sisend == listb[rn]:
            punktid[lista[rn]] += 1
        else:
            if punktid[lista[rn]] != 0:
                punktid[lista[rn]] -= 1
        if punktid[lista[rn]] == 2:
            lista.pop(rn)
            listb.pop(rn)
        rn = random.randint(0,len(lista) - 1)
        f.set(f"Sisestage sõna {lista[rn]} tõlge")
        r.set("")
    except:
        s.set("Said sõnad õpitud!")

r = StringVar()
s = StringVar()
f = StringVar()
meetod1l = Label(meetod1f, textvariable=s)
meetod1l2 = Label(meetod1f, textvariable=f)
meetod1e = tk.Entry(meetod1f,textvariable=r ,width = 30)

def meetod1():
    meetod1f.pack(fill='both', expand=1)
    greet.pack_forget()
    meetod1l2.pack()
    meetod1e.pack()
    meetod1l.pack()
    global s
    s.set("")
    r.set("")
    try:
        global rn
        rn = random.randint(0,len(lista) - 1)
        f.set(f"Sisestage sõna {lista[rn]} tõlge")
        meetod1e.bind("<Return>", comp_s)     
    except:
        s.set("")

#MEETOD 2
y = StringVar()
x = StringVar()
r1 = 0
r2 = 0
r3 = 1

def meetod3fun():
    try:        
        global r1
        global r2
        global r3
        if r3 == 1:
            if r1 == r2:    
                if vastus == 1:
                    y.set("Tubli")
                    akoopia.pop(r1)
                    bkoopia.pop(r1)
                else:
                    y.set("Vale vastus")
            else:
                if vastus == 0:
                    y.set("Õige vastus")
                elif vastus == 1:
                    y.set("Vale vastus")
            r1 = random.randint(0, len(lista) - 1)
            r2 = random.randint(0, len(listb) - 1)
            r3 = random.choice([0, 1])
            x.set(f"Kas {akoopia[r1]} tõlge on {bkoopia[r2]}?")
        else:
            if r1 == r2:
                if  vastus == 1:
                    y.set("Tubli")
                    akoopia.pop(r1)
                    bkoopia.pop(r2)
                else:
                    y.set("Vale vastus")
            else:
                if vastus == 0:
                    y.set("Tubli")
                else:
                    y.set("Vale vastus")
            r1 = random.randint(0, len(lista) - 1)
            r2 = random.randint(0, len(listb) - 1)
            r3 = random.choice([0, 1])
            x.set(f"Kas {akoopia[r1]} tõlge on {bkoopia[r2]}?")
    except:
        x.set("")
        y.set("Said hakkama!!")


def true():
    global vastus
    vastus = 1
    meetod3fun()

def false():
    global vastus
    vastus = 0
    meetod3fun()

def meetod3():
    global akoopia
    global bkoopia
    akoopia = lista
    bkoopia = listb
    meetod3f.pack(fill='both', expand=1)
    greet.pack_forget()
    meetod3l2.pack(pady=10)
    meetod3bt.pack()
    meetod3bf.pack()
    meetod3l1.pack(pady=10)
    y.set("")
    try:
        global r1
        global r2
        r1 = random.randint(0, len(lista) - 1)
        r2 = random.randint(0, len(listb) - 1)
        x.set(f"Kas {akoopia[r1]} tõlge on {bkoopia[r2]}?")
    except:
        x.set("")
        

meetod3l1 = Label(meetod3f, textvariable = y)
meetod3l2 = Label(meetod3f, textvariable = x)
meetod3bt = Button(meetod3f, text="TRUE", command = true)
meetod3bf = Button(meetod3f, text="FALSE", command = false)
vastus = 0 
    

font1 = font.Font(family='Georgia', size='12', weight='bold')
font2 = font.Font(family='Aerial', size='12')


label_text = "Saad valida kolme õppimismeetodi vahel.\n \
Esimene meetod annab sulle eestikeelse sõne ja sa pead selle tõlkima.\n \
Teine meetod annab sulle ette sõna ning sa pead vastama kas tõlge on õige või vale."

label1 = Label(greet, text=label_text, font=font1)
label1.pack(pady=20)

label2 = Label(order, text="Sisestage sõnad mida soovite õppida.", font=font2)
label2.pack(pady=20)

esilehele()

btn1 = Button(greet, text="Sõnu sisestama", font=font2, command=sõnu_sisestama)
btn1.pack(pady=20)

back_btn1 = Button(order, text="Esilehele", font=font2, command=esilehele)
back_btn1.pack(pady=20)

btn3 = Button(greet, text="Meetod 1", font=font2, command=meetod1)
btn3.pack(pady=10)

btn5 = Button(greet, text="Meetod 2", font=font2,command=meetod3)
btn5.pack(pady=10)

back_btn2 = Button(meetod1f, text="Esilehele", font=font2, command=esilehele)
back_btn2.pack(pady=20)

back_btn4 = Button(meetod3f, text="Esilehele", font=font2, command=esilehele)
back_btn4.pack(pady=20)



entry1 = tk.Text(order,height = 8, width = 20)
entry1.pack()
entry1.insert("1.0", data)


näita = Button(order, text = "Salvesta sõnad", font=font2, command = näita)
näita.pack(pady=10)

fail.close()
win.mainloop()