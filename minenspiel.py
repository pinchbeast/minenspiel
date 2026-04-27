import tkinter as tk
import random

def cazzo():
    counter = 0
    print("cazzo")
    for teil in tocheck:
        merda(teil, buttons[teil])


    

def merda(guesscode, btn):

    if(catalog[guesscode] == 0):
        print("guter guess")
        
        minenumbernearby=nearby(guesscode)
        btn.config(text=minenumbernearby)
    elif(catalog[guesscode] == 69):
        print("ALARM VERKACKT DU DEPP")
        btn.config(text="X", background="red")
    for teil in tocheck:
        print(teil)
    cazzo()

def nearby(orig):
    codes = [orig + 1, orig-1,orig+size,orig-size,orig + 1 + size, orig-1 + size,orig-size +1,orig-size-1]
    #codes.append([orig + 1], [orig-1],[orig+size],[orig-size])
    minenumbernearby = 0

    #this for tests every one of the nearby fields
    for nearfield in codes:

        if(catalog[nearfield] == 0):
            print("guter guess")
            buttons[nearfield].config(text="O")
            tocheck.append(nearfield)
        elif(catalog[nearfield] == 69):
            print("ALARM VERKACKT DU DEPP")
            minenumbernearby = minenumbernearby + 1
    return minenumbernearby


root = tk.Tk()
#here change size of the grid and set mines
size = 12
mines = 30
root.title("Minenspiel")
root.configure(background="white")
root.minsize(500, 500)
root.maxsize(1000, 1000)


tocheck = ([])
buttons = {}

for y in range(0, size):
    for x in range(0, size):
        guesscode = size * x + y
        buttonname = (f"button_{guesscode}")
        buttonname = tk.Button(root, text="", width=1, height=1)
        buttonname.config(command=lambda r=guesscode, b=buttonname:  merda(r,b))
        buttonname.grid(row=x, column=y)
        buttons[guesscode]=buttonname
 
ranger = size ** 2 + 1
catalog = [0] * ranger
stop = 0

for wtf in range(1, mines):
    stop = 0
    while(stop == 0):
        rand = random.randint(0, ranger-1)
        if(catalog[rand] == 0):
            catalog[rand] = 69
            stop = 1
        else:
            print("fuck")








root.mainloop()
