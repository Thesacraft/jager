import tkinter


def umrechnen():
    Euro = int(EingabeFeld.get())
    AusgabeFeld.delete("1.0", "end")
    Ausgabe = Euro * 1.042
    AusgabeFeld.insert("end", f"{round(Ausgabe, 2)} CHF")


Fenster = tkinter.Tk()
Fenster.title("Währungsrechner")

# Label
WillkommenLabel = tkinter.Label(Fenster, text="Willkommen im Währungsrechner :)")
WillkommenLabel.grid(row=0, column=0, padx=5, pady=5)
EuroLabel = tkinter.Label(Fenster, text="Geben Sie den zu umrechnenden Wert in Euro Ein:")
EuroLabel.grid(row=1, column=0, padx=5, pady=5)
SchweizLabel = tkinter.Label(Fenster, text="Ist in Schweizer Franken: ")
SchweizLabel.grid(row=3, column=0, padx=5, pady=5)
# EingabeFeld
EingabeFeld = tkinter.Entry(Fenster)
EingabeFeld.grid(row=1, column=1, padx=5, pady=5)
# Button
ButtonRechnen = tkinter.Button(Fenster, text="Umrechnen", command=umrechnen)
ButtonRechnen.grid(row=2, column=1, padx=5, pady=5)
# Ausgabe
AusgabeFeld = tkinter.Text(Fenster, height=1, width=20)
AusgabeFeld.grid(row=3, column=1, padx=5, pady=5)

Fenster.mainloop()
