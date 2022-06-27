from tkinter import *
# Ereignisbehandlung
global items
items = None
mehr = 0
def ueberraschen():
    global ueberraschung
    ueberraschung = not ueberraschung
    move_all()
def linksVerschieben():
    if(ueberraschung):
        boundrie = boundries[0][0]
    else:
        boundrie = boundries[1][0]
    if coords["base_coords"][0] >= boundrie:
        move([-10,0])

def rechtsVerschieben():
    if(ueberraschung):
        boundrie = boundries[0][1]
    else:
        boundrie = boundries[1][1]
    if coords["base_coords"][0] <= boundrie:
        move([10,0])

def obenVerschieben():
    if(ueberraschung):
        boundrie = boundries[0][2]
    else:
        boundrie = boundries[1][2]
    if coords["base_coords"][1] >= boundrie:
        move([0,-10])

def untenVerschieben():
    if(ueberraschung):
        boundrie = boundries[0][3]
    else:
        boundrie = boundries[1][3]
    if coords["base_coords"][1] <= boundrie:
        move([0,10])

def objektLoeschen():
    global mehr
    global canvas
    global items
    for item in items:
        canvas.delete(item)
    items = None
    mehr += 4
    
def objekterstellen():
    global items
    if items == None:
        global id_oval_wheel_1
        global id_oval_wheel_2
        global id_rechteck_oben
        global id_rechteck
        id_oval_wheel_1 = canvas.create_oval(-10,-10,-5,-5,fill="black")
        id_oval_wheel_2 = canvas.create_oval(-10,-10,-5,-5,fill="black")
        id_rechteck_oben = canvas.create_rectangle(-10, -10, -5, -5, fill="red")
        id_rechteck = canvas.create_rectangle(80, 30, 120, 40, fill="red")
        items=[id_oval_wheel_1,id_oval_wheel_2,id_rechteck_oben,id_rechteck]
        move_all()
        

boundries = [[25,565,20,330],[25,565,10,340]]
# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title("Leinwand")
tkFenster.geometry("600x400")
coords = {"base_coords":[100,35],4:[-20,-5,20,5],3:[-15,-5,15,-10],1:[-15,5,-10,10],2:[10,5,15,10]}
ueberraschung = False
def move(cords):
    coords["base_coords"][0] += cords[0]
    coords["base_coords"][1] += cords[1]
    move_all()
def move_all():
    if ueberraschung:
        for i in items:
            x0 = coords["base_coords"][0] + coords[i-mehr][0]
            y0 = coords["base_coords"][1] + coords[i-mehr][1]
            x1 = coords["base_coords"][0] + coords[i-mehr][2]
            y1 = coords["base_coords"][1] + coords[i-mehr][3]
            canvas.coords(i, (x0,y0,x1,y1))
    else:
        i = 4
        x0 = coords["base_coords"][0] + coords[i][0]
        y0 = coords["base_coords"][1] + coords[i][1]
        x1 = coords["base_coords"][0] + coords[i][2]
        y1 = coords["base_coords"][1] + coords[i][3]
        canvas.coords(items[3], (x0,y0,x1,y1))
        for i in items:
            if not i-mehr == 4:
                (x0,y0,x1,y1) = [-10,-10,-10,-10]
                canvas.coords(i, (x0,y0,x1,y1))

# Zeichenleinwand
canvas = Canvas(master=tkFenster, background="white")
canvas.place(x=5, y=5, width=590, height=350)
objekterstellen()
# Grafikobjekte

# Schaltfaechen
buttonLinks = Button(master=tkFenster, text="links", command=linksVerschieben)
buttonLinks.place(x=10,y=370,width=80,height=20)
buttonOben = Button(master=tkFenster, text="oben", command=obenVerschieben)
buttonOben.place(x=100,y=370,width=80,height=20)
buttonRechts = Button(master=tkFenster, text="rechts", command=rechtsVerschieben)
buttonRechts.place(x=190,y=370,width=80,height=20)
buttonUnten = Button(master=tkFenster, text="unten", command=untenVerschieben)
buttonUnten.place(x=280,y=370,width=80,height=20)
buttonLoeschen = Button(master=tkFenster, text="entfernen", command=objektLoeschen)
buttonLoeschen.place(x=370,y=370,width=80,height=20)
buttonerstellen = Button(master=tkFenster, text="erstellen", command=objekterstellen)
buttonerstellen.place(x=440,y=370,width=80,height=20)
buttonueberaschen = Button(master=tkFenster, text="Überraschung", command=ueberraschen)
buttonueberaschen.place(x=510,y=370,width=80,height=20)
# Aktivierung der Ereignisschleife
tkFenster.mainloop()
