from tkinter import *  
from random import randint

# Ereignisverarbeitung
def buttonWuerfelnClick():
    # Verwaltung und Verarbeitung der Daten
    augen = randint(1,6)
    # Anzeige der Daten
    labelWuerfel.config(image=Bilder[augen-1])
# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Würfeln')
tkFenster.geometry('430x270')
Bilder = []
# Bilder
for i in range(6):
    Bilder.append(PhotoImage(file=f"w{i+1}.gif"))

#Farbe für den Hintergrund (in einem Label erstellt)
labelBGFarbe = Label(tkFenster, bg='#FBD975')
labelBGFarbe.place(x=5, y=5, width = 420, height = 260)

# Label Würfel mit Bild
labelWuerfel = Label(tkFenster, image=Bilder[0]) 
labelWuerfel.place(x=140, y=40, width=150, height=150)

# Button zum Würfeln
buttonWuerfel = Button(tkFenster, text='würfeln', command=buttonWuerfelnClick)
buttonWuerfel.place(x=140, y=200, width=150, height=50)

# Aktivierung des Fensters
tkFenster.mainloop()
