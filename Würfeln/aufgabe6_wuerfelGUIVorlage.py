from random import randint
from tkinter import *


# Ereignisverarbeitung
def buttonWuerfelnClick():
    # Verwaltung und Verarbeitung der Daten
    augen = randint(1, 6)
    # Anzeige der Daten
    if augen == 1:
        labelWuerfel.config(image=imageWuerfel1)
    elif augen == 2:
        labelWuerfel.config(image=imageWuerfel2)
    elif augen == 3:
        labelWuerfel.config(image=imageWuerfel3)
    elif augen == 4:
        labelWuerfel.config(image=imageWuerfel4)
    elif augen == 5:
        labelWuerfel.config(image=imageWuerfel5)
    elif augen == 6:
        labelWuerfel.config(image=imageWuerfel6)


# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Würfeln')
tkFenster.geometry('430x270')

# Bilder
imageWuerfel1 = PhotoImage(file='w1.gif')
imageWuerfel2 = PhotoImage(file='w2.gif')
imageWuerfel3 = PhotoImage(file='w3.gif')
imageWuerfel4 = PhotoImage(file='w4.gif')
imageWuerfel5 = PhotoImage(file='w5.gif')
imageWuerfel6 = PhotoImage(file='w6.gif')

# Farbe für den Hintergrund (in einem Label erstellt) Author: www.github.com/Thesacraft
labelBGFarbe = Label(tkFenster, bg='#FBD975')
labelBGFarbe.place(x=5, y=5, width=420, height=260)

# Label Würfel mit Bild
labelWuerfel = Label(tkFenster, image=imageWuerfel1)
labelWuerfel.place(x=140, y=40, width=150, height=150)

# Button zum Würfeln
buttonWuerfel = Button(tkFenster, text='würfeln', command=buttonWuerfelnClick)
buttonWuerfel.place(x=140, y=200, width=150, height=50)

# Aktivierung des Fensters
tkFenster.mainloop()
