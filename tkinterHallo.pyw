import tkinter

# GUI Anfang
Fenster = tkinter.Tk()
Fenster.title("Begrüßung")

# Entry (Eingabefeld)
EingabeFeld = tkinter.Entry(Fenster, width=40)
EingabeFeld.grid(row=1, column=0, padx=5, pady=5)

# Text (Ausgabefeld für Texte)
AusgabeFeld = tkinter.Text(Fenster, width=30, height=15)
AusgabeFeld.grid(row=3, column=0, padx=5, pady=5)


def ButtonGrussClick():
    # Code für Prozedur
    Name = EingabeFeld.get()
    AusgabeFeld.delete("1.0", "end")
    AusgabeFeld.insert("end", "Hallo " + Name + '!')


# Button (Verarbeitung) -> bei Click wird Prozedur ausgeführt
ButtonGruss = tkinter.Button(Fenster, text=" Begrüßung ", command=
ButtonGrussClick)
ButtonGruss.grid(row=2, column=0, padx=5, pady=10)

# GUI Ende
Fenster.mainloop()
