'''
LeinwandCanvas-AmpelGUI.py
18.6.22
Author: www.github.com/Thesacraft
'''

from tkinter import *


# Ereignisbehandlung
def buttonWeiterClick():
    if canvas.itemcget(id_rot, 'fill') == 'red' and \
            canvas.itemcget(id_gruen, 'fill') == 'gray':
        # aktueller Zustand: rot
        # naechster Zustand: grün
        canvas.itemconfigure(id_rot, fill='gray')
        canvas.itemconfigure(id_gruen, fill='green')
    elif canvas.itemcget(id_rot, 'fill') == 'gray' and \
            canvas.itemcget(id_gruen, 'fill') == 'green':
        # aktueller Zustand: grün
        # naechster Zustand: rot
        canvas.itemconfigure(id_rot, fill='red')
        canvas.itemconfigure(id_gruen, fill='gray')


# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Ampel')
tkFenster.geometry('170x240')

# Zeichenfläche
canvas = Canvas(tkFenster, bg='blue')
canvas.place(x=5, y=5, width=160, height=160)

# Ampelkasten Author: www.github.com/Thesacraft
canvas.create_rectangle(65, 10, 95, 80, fill='black')
# Stange
canvas.create_rectangle(78, 80, 82, 150, fill='black')
# Rot-Licht
id_rot = canvas.create_oval(70, 20, 90, 40, fill='red')
# Grün-Licht
id_gruen = canvas.create_oval(70, 50, 90, 70, fill='gray')

# Button zum Weiterschalten
buttonWeiter = Button(tkFenster, text='weiter', command=buttonWeiterClick)
buttonWeiter.place(x=5, y=210, width=160, height=20)

# Ereignisschleife starten
tkFenster.mainloop()
