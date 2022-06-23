from random import randint
from tkinter import *

root = Tk()
root.title("Zahlenranten")
global rateversuche
rateversuche = 0


def generate():
    global rateversuche
    rateversuche = 0
    global zufallszahl
    zufallszahl = randint(1, 100)


generate_Button = Button(root, text="Zuffalszahl erzeugen", command=generate)
generate_Button.grid(row=0, column=0)
Eingabe = Entry(root)
Eingabe.grid(row=1, column=0)
Ausgabe = Text(root)
Ausgabe.grid(row=3, column=0)


def naehe():
    tipp = int(Eingabe.get())
    print(tipp)
    global rateversuche
    rateversuche += 1
    if tipp > zufallszahl:
        Ausgabe.delete("1.0", "end")
        Ausgabe.insert("end", "Ihre Zahl ist zu Groß.")
    elif tipp < zufallszahl:
        Ausgabe.delete("1.0", "end")
        Ausgabe.insert("end", "Ihre Zahl ist zu klein.")
    elif tipp == zufallszahl:
        Ausgabe.delete("1.0", "end")
        Ausgabe.insert("end", f"Richtig. Es ist: {zufallszahl} \nSie haben {rateversuche} gebraucht")


ueberpreufen_Button = Button(root, text="Rateversuch", command=naehe)
ueberpreufen_Button.grid(row=2, column=0)
root.mainloop()
