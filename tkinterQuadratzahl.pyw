from tkinter import *

root = Tk()
root.title("Quadratzahlberechnung")

Eingabe = Entry(root)
Eingabe.grid(row=0, column=0)
Ausgabe = Text(root)
Ausgabe.grid(row=2, column=0)


def berechnung():
    a = float(Eingabe.get())
    quadratzahl = a * a
    Ausgabe.delete("1.0", "end")
    Ausgabe.insert("end", f"Die Quadratzahl beträgt: {quadratzahl}")


berechnung_Button = Button(root, text="Quadratzahl", command=berechnung)
berechnung_Button.grid(row=1, column=0)
root.mainloop()
