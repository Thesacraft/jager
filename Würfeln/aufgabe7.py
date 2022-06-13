from tkinter import *
from random import randint


root = Tk()
root.geometry("300x180")
root.title("Schere Stein Papier")

def play():
    rand = randint(1,3)
    LabelHand.config(image=Bilder[rand-1])
    
Bilder = []
for i in range(3):
    Bilder.append(PhotoImage(file=f"stp{i+1}.png"))

LabelHand = Label(root,image=Bilder[1])
LabelHand.place(x=75,y=0,height=150,width=150)
spielenButton = Button(root,text="Spielen",command=play)
spielenButton.place(x=75,y=150,height=30,width=150)
root.mainloop()