import tkinter as tk



def merda(h,w):

    print("button mit koordinaten: x", h,"y", w, "wurde gedrückt")


root = tk.Tk()
#here change size of the grid
size = 12
root.title("Minenspiel")
root.configure(background="white")
root.minsize(500, 500)
root.maxsize(1000, 1000)

counter = 0
array = ([])

#create array from 1-size
while(counter < size):
    array.append(counter)
    counter = counter + 1



# x = row, counter = column

for y in array:
    for x in array:
        buttonname = (f"button_{x}_{y}")
        buttonname = tk.Button(root, text="o", width=1, height=1, command=lambda r=y, c=x: merda(r,c))
        buttonname.grid(row=x, column=y)
 

#b1a = tk.Button(root, text="o", width=2, height=2, command=lambda: merda(1,1)).pack()





root.mainloop()
