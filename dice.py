import random
from tkinter import *
n = random.randint(1,6)
root =  Tk()
img = PhotoImage(file = 'dicee.png')
Label(root,image=img).pack()
root.title("Dice_Simulator")
root.iconbitmap("doice.ico")
l  = Label(text = n)
l.pack()
root.mainloop()