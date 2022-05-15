"""
Autor:SB
Datum: 30.01.2022
comment: Dieses Programm mischt die karten und teilt 5 karten jeweils einem spieler zu
"""


import random


#Deklarieren der Variablen
Spielkarten = ["HA","HK","HD","HB","H10","H9","H8","KA","KK","KD","KB","K10","K9","K8","KRA","KRK","KRD","KRB","KR10","KR9","KR8","PA","PK","PD","PB","P10","P9","P8"]
Spielkartenvorher = ["HA","HK","HD","HB","H10","H9","H8","KA","KK","KD","KB","K10","K9","K8","KRA","KRK","KRD","KRB","KR10","KR9","KR8","PA","PK","PD","PB","P10","P9","P8"]
Spielkartengemischt = []
Spielkartenanzahl = len(Spielkarten)

#Mischen
for i in range(Spielkartenanzahl):
    temp_Spielkarte = random.choice(Spielkarten)
    Spielkarten.remove(temp_Spielkarte)
    Spielkartengemischt.append(temp_Spielkarte)
    temp_Spielkarte = ""
    
#Ausgeben der gemischten und nicht gemischten Karten
print(f"\nGemischte Spielkarten:{Spielkartengemischt}\n\nnicht Gemischte Spielkarten: {Spielkartenvorher}\n")

#Austeilen
def Spielerkarten():
    Spieler_karten = []
    for i in range(5):
        Spieler_karten.append(Spielkartengemischt[0])
        Spielkartengemischt.pop(0)
    return(Spieler_karten)

Spieler1 = Spielerkarten()
Spieler2 = Spielerkarten()
Spieler3 = Spielerkarten()
#Ausgabe
print(f"Spieler1 hat die Karten: {Spieler1}\nSpieler2 hat die Karten: {Spieler2}\nSpieler3 hat die Karten: {Spieler3}\nDer Stapel enthält die Karten: {Spielkartengemischt}")

 
