# Programmname: anhalteweg.py


# Definition der Funktion
def Berechnungen(geschwindigkeit):
    reaktionsweg = (geschwindigkeit / 10) * 3
    bremsweg = (geschwindigkeit / 10) * (geschwindigkeit / 10)
    anhalteweg = bremsweg + reaktionsweg
    return reaktionsweg, bremsweg, anhalteweg


# Eingabe
eingabe_geschwindigkeit = int(input(f"Geben sie ihre Geschwindigkeit in km/h an: "))

# Verarbeitung und aufrufen der Funktion
[ausgabe_reaktionsweg, ausgabe_bremsweg, ausgabe_anhalteweg] = Berechnungen(eingabe_geschwindigkeit)

# Ausgabe
print(f"Reaktionsweg: {ausgabe_reaktionsweg}")
print(f"Bremsweg: {ausgabe_bremsweg}")
print(f"Anhalteweg: {ausgabe_anhalteweg}")
