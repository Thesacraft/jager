"""
Autor:SB
Datum: 30.01.2022
comment: Dieses Programm simuliert das Spiel 17 und 4
"""

import random

# Deklarieren der Variablen
Spielkarten = ["HA", "HK", "HD", "HB", "H10", "H9", "H8", "KA", "KK", "KD", "KB", "K10", "K9", "K8", "KRA", "KRK",
               "KRD", "KRB", "KR10", "KR9", "KR8", "PA", "PK", "PD", "PB", "P10", "P9", "P8"]
Spielkarten_werte = {"HA": 11, "HK": 4, "HD": 3, "HB": 2, "H10": 10, "H9": 9, "H8": 8, "KA": 11, "KK": 4, "KD": 3,
                     "KB": 2, "K10": 10, "K9": 9, "K8": 8, "KRA": 11, "KRK": 4, "KRD": 3, "KRB": 2, "KR10": 10,
                     "KR9": 9, "KR8": 8, "PA": 11, "PK": 4, "PD": 3, "PB": 2, "P10": 10, "P9": 9, "P8": 8}
Spielkartengemischt = []
Spielkartenanzahl = len(Spielkarten)
Spieler1_karten = []
Spieler1_summe = 0
Spieler2_karten = []
Spieler2_summe = 0

# Mischen
for i in range(Spielkartenanzahl):
    Spielkartengemischt.append(random.choice(Spielkarten))
    Spielkarten.remove(Spielkartengemischt[len(Spielkartengemischt) - 1])


# summe berechnen
def summe_karten(spielerkarten):
    summe = 0
    for karte in spielerkarten:
        summe += Spielkarten_werte[karte]
    return (summe)


# Spieler1 Spielt
while True:
    Spieler1_karten.append(Spielkartengemischt.pop(0))
    print(f"Spieler1 du hast jetzt die Karten:\n{Spieler1_karten}")
    if len(Spieler1_karten) > 1:
        antwort = input("Spieler1 willst du noch eine Karte ziehen?(ja/nein)")
    else:
        antwort = "ja"
    if not antwort.lower() == "ja":
        break

# überprüfen ob er direkt verloren oder gewonnen hat
Spieler1_summe = summe_karten(Spieler1_karten)
if (Spieler1_summe == 21):
    print("Spieler1 hat gewonnen!")
    exit()
elif (Spieler1_summe > 21):
    print("Spieler1 hat verloren")
    exit()

# Spieler2 spielt
while True:
    Spieler2_karten.append(Spielkartengemischt.pop(0))
    print(f"Spieler2 du hast jetzt die Karten:\n{Spieler2_karten}")
    if len(Spieler2_karten) > 1:
        antwort = input("Spieler2 willst du noch eine Karte ziehen?(ja/nein)")
    else:
        antwort = "ja"
    if not antwort.lower() == "ja":
        break

# Ausgeben und überprüfen wer von beiden gewonnen hat
Spieler2_summe = summe_karten(Spieler2_karten)

print(
    f"\nDie summe von den karten von Spieler1 ist: {Spieler1_summe}\nDie summe von den karten von Spieler2 ist: {Spieler2_summe}\n")
if (Spieler2_summe < Spieler1_summe):
    print("Spieler1 hat gewonnen")
elif (Spieler2_summe <= 21):
    print("Spieler2 hat gewonnen")
else:
    print("Spieler1 hat gewonnen")
