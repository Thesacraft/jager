from tkinter import *

root = Tk()
root.title("Berechnung für einen Quader")
# Label's
label_laenge = Label(root, text="Länge")
label_laenge.grid(row=0, column=0, padx=5, pady=5)
label_hoehe = Label(root, text="Hoehe")
label_hoehe.grid(row=1, column=0, padx=5, pady=5)
label_breite = Label(root, text="Breite")
label_breite.grid(row=2, column=0, padx=5, pady=5)
label_oberflaeche = Label(root, text="Oberfläche")
label_oberflaeche.grid(row=4, column=0, padx=5, pady=5)
label_volumen = Label(root, text="Volumen")
label_volumen.grid(row=5, column=0, padx=5, pady=5)
# Entry's
entry_laenge = Entry(root)
entry_laenge.grid(row=0, column=1, padx=5, pady=5)
entry_hoehe = Entry(root)
entry_hoehe.grid(row=1, column=1, padx=5, pady=5)
entry_breite = Entry(root)
entry_breite.grid(row=2, column=1, padx=5, pady=5)
# Text
text_oberflaeche = Text(root, height=1, width=30)
text_oberflaeche.grid(row=4, column=1, padx=5, pady=5)
text_volumen = Text(root, height=1, width=30)
text_volumen.grid(row=5, column=1, padx=5, pady=5)


# functions
def berechnen():
    laenge = float(entry_laenge.get())
    hoehe = float(entry_hoehe.get())
    breite = float(entry_breite.get())
    Volumen = breite * hoehe * laenge
    Oberflaeche = breite * hoehe * 2 + breite * laenge * 2 + laenge * hoehe * 2
    text_oberflaeche.delete("1.0", "end")
    text_volumen.delete("1.0", "end")
    text_oberflaeche.insert("end", Oberflaeche)
    text_volumen.insert("end", Volumen)


# Button's
berechnen_button = Button(root, text="berechnen", command=berechnen)
berechnen_button.grid(row=3, column=1, padx=5, pady=5)
# GUI mainloop
root.mainloop()
