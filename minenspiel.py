import tkinter as tk



def merda(h,w):

    print("button mit koordinaten: ", h, w, "wurde gedrückt")


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

while(counter > 0):
    for x in array:
        buttonname = (f"button_{x}_{counter}")
        buttonname = tk.Button(root, text="o", width=1, height=1, command=lambda r=counter, c=x: merda(r,c))
        buttonname.grid(row=x, column=counter)
        


    counter = counter - 1    



#b1a = tk.Button(root, text="o", width=2, height=2, command=lambda: merda(1,1)).pack()





root.mainloop()
