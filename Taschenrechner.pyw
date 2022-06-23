import tkinter

Zahl1 = 0
Operator = "leer"


# Prozeduren für die Zahlentasten
def B0Click():
    a = EinAusgabe.get()
    EinAusgabe.delete(0, "end")
    EinAusgabe.insert(0, a + "0")


def B1Click():
    a = EinAusgabe.get()
    EinAusgabe.delete(0, "end")
    EinAusgabe.insert(0, a + "1")


def B2Click():
    a = EinAusgabe.get()
    EinAusgabe.delete(0, "end")
    EinAusgabe.insert(0, a + "2")


def B3Click():
    a = EinAusgabe.get()
    EinAusgabe.delete(0, "end")
    EinAusgabe.insert(0, a + "3")


def B4Click():
    a = EinAusgabe.get()
    EinAusgabe.delete(0, "end")
    EinAusgabe.insert(0, a + "4")


def B5Click():
    a = EinAusgabe.get()
    EinAusgabe.delete(0, "end")
    EinAusgabe.insert(0, a + "5")


def B6Click():
    a = EinAusgabe.get()
    EinAusgabe.delete(0, "end")
    EinAusgabe.insert(0, a + "6")


def B7Click():
    a = EinAusgabe.get()
    EinAusgabe.delete(0, "end")
    EinAusgabe.insert(0, a + "7")


def B8Click():
    a = EinAusgabe.get()
    EinAusgabe.delete(0, "end")
    EinAusgabe.insert(0, a + "8")


def B9Click():
    a = EinAusgabe.get()
    EinAusgabe.delete(0, "end")
    EinAusgabe.insert(0, a + "9")


# Prozeduren für die Rechentasten
def BPlusClick():
    global Zahl1
    global Operator
    if Zahl1 == 0 or Zahl1 == None:  # Überprüfen ob Zahl1 schon einen wert hat um laengere Rechnungen besser moeglich zu machen
        Zahl1 = int(EinAusgabe.get())  # erste Zahl merken
        EinAusgabe.delete(0, "end")  # Eingabefeld leeren
        Operator = "+"  # Rechentaste merken
    else:
        BGleichClick()
        BPlusClick()


def BMinusClick():
    global Zahl1
    global Operator
    if Zahl1 == 0 or Zahl1 == None:  # Überprüfen ob Zahl1 schon einen wert hat um laengere Rechnungen besser moeglich zu machen
        Zahl1 = int(EinAusgabe.get())  # erste Zahl merken
        EinAusgabe.delete(0, "end")  # Eingabefeld leeren
        Operator = "-"  # Rechentaste merken
    else:
        BGleichClick()
        BMinusClick()


def BMalClick():
    global Zahl1
    global Operator
    if Zahl1 == 0 or Zahl1 == None:  # Überprüfen ob Zahl1 schon einen wert hat um laengere Rechnungen besser moeglich zu machen
        Zahl1 = int(EinAusgabe.get())  # erste Zahl merken
        EinAusgabe.delete(0, "end")  # Eingabefeld leeren
        Operator = "*"  # Rechentaste merken
    else:
        BGleichClick()
        BMalClick()


def BDurchClick():
    global Zahl1
    global Operator
    if Zahl1 == 0 or Zahl1 == None:  # Überprüfen ob Zahl1 schon einen wert hat um laengere Rechnungen besser moeglich zu machen
        Zahl1 = int(EinAusgabe.get())  # erste Zahl merken
        EinAusgabe.delete(0, "end")  # Eingabefeld leeren
        Operator = "/"  # Rechentaste merken
    else:
        BGleichClick()
        BDurchClick()


def show(Ergebnis):
    global Zahl1
    Zahl1 = 0
    EinAusgabe.delete(0, "end")
    EinAusgabe.insert(0, Ergebnis)


# Prozeduren für die =-Taste und die Clear-Taste
def BGleichClick():
    global Zahl1
    global Operator
    if (Operator == "+"):
        Ergebnis = Zahl1 + int(EinAusgabe.get())
        show(Ergebnis)
    if (Operator == "-"):
        Ergebnis = Zahl1 - int(EinAusgabe.get())
        show(Ergebnis)
    if (Operator == "*"):
        Ergebnis = Zahl1 * int(EinAusgabe.get())
        show(Ergebnis)
    if (Operator == "/"):
        Ergebnis = int(Zahl1 / int(EinAusgabe.get()))
        show(Ergebnis)


def BClearClick():
    EinAusgabe.delete(0, "end")
    Zahl1 = 0


# GUI Anfang
# Fenster anlegen
Fenster = tkinter.Tk()
Fenster.title('Taschenrechner')
Fenster.geometry('300x200')
# Ein-/Ausgabefeld anlegen
EinAusgabe = tkinter.Entry(Fenster, width=30, justify=
tkinter.RIGHT)
EinAusgabe.grid(row=0, column=0, columnspan=4, padx=5,
                pady=5)
# Layout des Taschenrechners mit allen Buttons
B1 = tkinter.Button(Fenster, text=" 1 ", command=B1Click)
B1.grid(row=1, column=0, padx=5, pady=5)
B2 = tkinter.Button(Fenster, text=" 2 ", command=B2Click)
B2.grid(row=1, column=1, padx=5, pady=5)
B3 = tkinter.Button(Fenster, text=" 3 ", command=B3Click)
B3.grid(row=1, column=2, padx=5, pady=5)
B4 = tkinter.Button(Fenster, text=" 4 ", command=B4Click)
B4.grid(row=2, column=0, padx=5, pady=5)
B5 = tkinter.Button(Fenster, text=" 5 ", command=B5Click)
B5.grid(row=2, column=1, padx=5, pady=5)
B6 = tkinter.Button(Fenster, text=" 6 ", command=B6Click)
B6.grid(row=2, column=2, padx=5, pady=5)
B7 = tkinter.Button(Fenster, text=" 7 ", command=B7Click)
B7.grid(row=3, column=0, padx=5, pady=5)
B8 = tkinter.Button(Fenster, text=" 8 ", command=B8Click)
B8.grid(row=3, column=1, padx=5, pady=5)
B9 = tkinter.Button(Fenster, text=" 9 ", command=B9Click)
B9.grid(row=3, column=2, padx=5, pady=5)
B0 = tkinter.Button(Fenster, text=" 0 ", command=B0Click)
B0.grid(row=4, column=1, padx=5, pady=5)

BPlus = tkinter.Button(Fenster, width=5, text=" + ",
                       command=BPlusClick)
BPlus.grid(row=1, column=3, padx=5, pady=5)
BMinus = tkinter.Button(Fenster, width=5, text=" - ",
                        command=BMinusClick)
BMinus.grid(row=2, column=3, padx=5, pady=5)
BMal = tkinter.Button(Fenster, width=5, text=" * ",
                      command=BMalClick)
BMal.grid(row=3, column=3, padx=5, pady=5)
BDurch = tkinter.Button(Fenster, width=5, text=" / ",
                        command=BDurchClick)
BDurch.grid(row=4, column=3, padx=5, pady=5)
BGleich = tkinter.Button(Fenster, width=5, text="  =  ",
                         command=BGleichClick)
BGleich.grid(row=4, column=4, padx=5, pady=5)
BClear = tkinter.Button(Fenster, width=5, text=" Clear ",
                        command=BClearClick)
BClear.grid(row=0, column=4, padx=5, pady=5)

# GUI Ende
Fenster.mainloop()
