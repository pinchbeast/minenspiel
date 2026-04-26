import tkinter as tk
import random



def merda(h,w, btn):

    print("button mit koordinaten: x", h,"y", w, "wurde gedrückt")
    guesscode = size * (w) + (h+1)
    if(catalog[guesscode] == 0):
        print("guter guess")
        btn.config(text="O")
    elif(catalog[guesscode] == 69):
        print("ALARM VERKACKT DU DEPP")
        btn.config(text="X", background="red")



root = tk.Tk()
#here change size of the grid and set mines
size = 4
mines = 5
root.title("Minenspiel")
root.configure(background="white")
root.minsize(500, 500)
root.maxsize(1000, 1000)



# x = row, counter = column

for y in range(0, size):
    for x in range(0, size):
        buttonname = (f"button_{x}_{y}")
        buttonname = tk.Button(root, text="", width=1, height=1)
        buttonname.config(command=lambda r=y, c=x, b=buttonname: merda(r,c,b))
        buttonname.grid(row=x, column=y)
 
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
