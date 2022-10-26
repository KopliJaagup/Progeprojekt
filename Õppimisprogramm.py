import random 

eesti =["tere", "puu", "klass"]
vöörkeel = ["hello", "tree", "class"]
"""
while True:
    a = input("Sisestage eesikeelne sõna: ")
    if a == "":
        break
    b = input("Sisestage vöörkeelne vaste: ")
    eesti.append(a)
    vöörkeel.append(b)
    print("----------------------------------")
""" 
print("Õppimise meetodid: ")

def meetod1(eesti, vöörkeel):
    a = eesti
    b = vöörkeel
    punktid = {}
    for n in a:
        punktid.update({n:0})
    print(punktid)
    while True:
        try:
            r = random.randint(0,len(a) - 1)
            print(r)
            sisend = input(f"Sisestage sõna {a[r]} tõlge: ")
            print(b[r])
            if sisend == b[r]:
                punktid[a[r]] += 1
                print("tubli")
            else:
                if punktid[a[r]] != 0:
                    punktid[a[r]] -= 1
            if punktid[a[r]] == 2:
                a.pop(r)
                b.pop(r)
            print(punktid)
        except:
            print("Said sõnad õpitud!")
            break
        
def truefalse(eesti, vöörkeel):
    a = eesti
    b = vöörkeel
    while True:
        try:
            r1 = random.randint(0, len(a) - 1)
            r2 = random.randint(0, len(b) - 1)
            r3 = random.choice([0,1])
            if r3 == 1:
                sisend = input(f"Kas {a[r1]} tõlge on {b[r1]}?(True or False)")
                print(r1,r2)
                if r1 == r1:    
                    if sisend == "True":
                        print("Tubli")
                        a.pop(r1)
                        b.pop(r1)
                        print(a)
                        print(b)
                    else:
                        print("Vale vastus")
                else:
                    if sisend == "False":
                        print("Õige vastus")
                    elif sisend == "True":
                        print("Vale vastus") 
            else:
                sisend = input(f"Kas {a[r1]} tõlge on {b[r2]}?")
                print(a,b)
                print(r1,r2)
                if r1 == r2:
                    if sisend == "True":
                        print("Tubli")
                        a.pop(r1)
                        b.pop(r2)
                    else:
                        print("Vale vastus")
                else:
                    if sisend == "False":
                        print("Tubli")
                    else:
                        print("Vale vastus")
        except:
            print("Said hakkama!!")
            break
        
        
truefalse(eesti, vöörkeel)
