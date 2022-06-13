#Programm zur Berechnung des BMIs

def berechnen(masse,groesse):
    groesse = groesse / 100
    bmi = round(masse /( groesse * groesse),2)
    return bmi

def Augabe(bmi):
    print(f"Ihr BMI beträgt: {BMI}")
    if bmi < 19:
        print("Sie sind Untergewichtig!")
    elif bmi >= 19 and bmi <= 26:
        print("Sie sind Normalgewichtig!")
    else:
        print("Sie sind Übergewichtig")

groesse = float(input("Geben Sie ihre Größe in cm an. "))
masse = float(input("Geben Sie ihr Gewicht in kg an. "))

BMI = berechnen(masse,groesse)
Augabe(BMI)