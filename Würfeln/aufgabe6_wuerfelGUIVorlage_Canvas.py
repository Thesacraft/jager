from tkinter import *  
from random import randint

# Ereignisverarbeitung
def buttonWuerfelnClick():
    # Verwaltung und Verarbeitung der Daten
    augen = randint(1,6)
    # Anzeige der Daten
    ButtonWuerfel.config(image=Bilder[augen-1])
# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Würfeln')
tkFenster.geometry('800x600')
Bilder = []
# Bilder
ImageHintergrund = PhotoImage(file="WuerfelTisch-oldthing.de.gif")
canvasBG = Canvas(tkFenster)
canvasBG.place(x=0,y=0,width=800,height=600)
canvasBG.create_image(0,0,image=ImageHintergrund,anchor='nw')


for i in range(6):
    Bilder.append(PhotoImage(file=f"w{i+1}.gif"))


# Label Würfel mit Bild
ButtonWuerfel = Button(tkFenster, image=Bilder[0],command=buttonWuerfelnClick) 
ButtonWuerfel.place(x=325, y=140, width=150, height=150)

# Button zum Würfeln

# Aktivierung des Fensters
tkFenster.mainloop()
