'''
VorlageSpielkartenMischenVerteilenGUI.py
'''

import random
from tkinter import *
global GemischteKarten
GemischteKarten = []

def mischen():
    # die Liste "Spielkarten" ist im Hauptprogramm definiert
    # hier wird mit der Kopie "SpielkartenKopie" gearbeitet
    # die Liste "GemischteKarten" soll in dieser Prozedur
    # unter Zuhilfenahme des random.randint - Befehls
    # erstellt werden 
    SpielkartenKopie = Spielkarten[:]
    global GemischteKarten
    GemischteKarten = []
    for i in range(len(SpielkartenKopie)):
        GemischteKarten.append(SpielkartenKopie.pop(SpielkartenKopie.index(random.choice(SpielkartenKopie))))
    print(GemischteKarten)

def Austeilen():
    if len(GemischteKarten) < 12:
        mischen()
    # die Karten werden reihum an die Spieler verteilt,
    # jeder Spieler erhält der Reihe nach insgesamt 3 Karten
    Spieler1 = []
    Spieler2 = []
    Spieler3 = []
    
    for i in range(3):
        Spieler1.append(GemischteKarten.pop(0))
        Spieler2.append(GemischteKarten.pop(0))
        Spieler3.append(GemischteKarten.pop(0))
    
    # Ausgabe der Spielerkarten zur Kontrolle
    print (Spieler1)
    print (Spieler2)
    print (Spieler3)
    
    # Weise die Grafiken der Spielkarten zu, damit sie
    # in der GUI angezeigt und positioniert werden
    GrafikZuweisen(Spieler1,Spieler2,Spieler3)
    
def EinzelneKarteZuweisen(Karte):
    # Gebe die Position der Karte in der Liste Spielkarten aus
    # Wähle dann aus der ImageListe das Author:https://github.com/thesacraft entsprechende Spielkartenbild aus
    KartePos = Spielkarten.index(Karte)
    ImageAktuell = ImageListe[KartePos]
    return (ImageAktuell)

def GrafikZuweisen(S1,S2,S3):
    
    # (TODO) ... trage geeignete Positionswerte für die erste
    # Karte eines jeden Spielers ein ...
    
    # Position erste Karte Spieler 1
    x1 = 80
    y1 = 240
    # Position erste Karte Spieler 2
    x2 = 250
    y2 = 80
    # Position erste Karte Spieler 3
    x3 = 410
    y3 = 240

    for i in range(3):
        # Erstelle in der Canvas das Bild der Karte von Spieler 1
        Bild = EinzelneKarteZuweisen(S1[i])
        canvas.create_image(x1, y1, image = Bild, anchor = 'nw')
        x1 += 20 # nach rechts gehen für die nächste Karte
        Bild = EinzelneKarteZuweisen(S2[i])
        canvas.create_image(x2, y2, image = Bild, anchor = 'nw')
        x2 += 20 # nach rechts gehen für die nächste Karte
        Bild = EinzelneKarteZuweisen(S3[i])
        canvas.create_image(x3, y3, image = Bild, anchor = 'nw')
        x3 += 20 # nach rechts gehen für die nächste Karte
        # (TODO) ...ergänze hier analog wie oben die Anzeige der Bildkarten
        # für Spieler 2 und Spieler 3...

#Hauptprogramm

#Spielkarten definieren
global Spielkarten
Spielkarten = ["HA","H10","HK","HD","HB","H9","H8","H7",\
               "KA","K10","KK","KD","KB","K9","K8","K7",\
               "KAA","KA10","KAK","KAD","KAB","KA9","KA8","KA7",\
               "PA","P10","PK","PD","PB","P9","P8","P7"]



# GUI
tkFenster = Tk()
tkFenster.title('Animation')
tkFenster.geometry('600x600')


# ImageListe in der Reihenfolge wie in der Liste Spielkarten anlegen, damit man
# über die Indices der Liste Spielkarten auf das passende Bild in der ImageListe
# zugreifen kann

ImageListe = [
    PhotoImage(file='HA.png'),
    PhotoImage(file='H10.png'),
    PhotoImage(file='HK.png'),
    PhotoImage(file='HD.png'),
    PhotoImage(file='HB.png'),
    PhotoImage(file='H9.png'),
    PhotoImage(file='H8.png'),
    PhotoImage(file='H7.png'),
    PhotoImage(file='KA.png'),
    PhotoImage(file='K10.png'),
    PhotoImage(file='KK.png'),
    PhotoImage(file='KD.png'),
    PhotoImage(file='KB.png'),
    PhotoImage(file='K9.png'),
    PhotoImage(file='K8.png'),
    PhotoImage(file='K7.png'),
    PhotoImage(file='KAA.png'),
    PhotoImage(file='KA10.png'),
    PhotoImage(file='KAK.png'),
    PhotoImage(file='KAD.png'),
    PhotoImage(file='KAB.png'),
    PhotoImage(file='KA9.png'),
    PhotoImage(file='KA8.png'),
    PhotoImage(file='KA7.png'),
    PhotoImage(file='PA.png'),
    PhotoImage(file='P10.png'),
    PhotoImage(file='PK.png'),
    PhotoImage(file='PD.png'),
    PhotoImage(file='PB.png'),
    PhotoImage(file='P9.png'),
    PhotoImage(file='P8.png'),
    PhotoImage(file='P7.png')
    ]


#Leinwand
canvas = Canvas(tkFenster, width=600, height=600)
canvas.place(x=0,y=0)

#Spieltisch

canvas.configure(bg="brown")
canvas.create_oval(40,40,560,560,fill="green")

#Buttons zum Mischen und zum Austeilen
mischenBT = Button(tkFenster,text="Mischen",command=mischen)
austeilenBT = Button(tkFenster,text="Austeilen",command=Austeilen,width=10)
mischenBT.place(x=40,y=20)
austeilenBT.place(x=500,y=20)
#Kartenhinterteil

photo = PhotoImage(file="hinten.png")
canvas.create_image(260, 400, image = photo, anchor = 'nw')

# Ereignisschleife starten
tkFenster.mainloop()