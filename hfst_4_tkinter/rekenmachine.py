# Importeer tkinter module. Geef naam tk.
import tkinter as tk
from functools import partial

getal1 = 0
getal2 = 0
operator = '0'
uitrekenen = False
clear = False
# Maak een lege GUI aan.
venster = tk.Tk()
def getal(getal):
    global getal1
    global getal2
    global operator
    global clear
    global uitrekenen
    print(getal)
    print(operator)
# Label aanmaken.
    # master: geef aan tot welke GUI het label behoort.
    # text: boodschap van het label.
veld = tk.Entry(master=venster, bg="green")  # maak een nieuw invulvlak
veld.grid(row=0, column=0, columnspan=3)

getalfunctie = partial(getal,1)
knop1 = tk.Button(master=venster, text="1", width=5, command=getalfunctie)
knop1.grid(row=1, column=0)

getalfunctie = partial(getal,2)
knop2 = tk.Button(master=venster, text="2", width=5, command=getalfunctie)
knop2.grid(row=1, column=1)

getalfunctie = partial(getal,3)
knop3 = tk.Button(master=venster, text="3", width=5, command=getalfunctie)
knop3.grid(row=1, column=2)

getalfunctie = partial(getal,4)
knop4 = tk.Button(master=venster, text="4", width=5, command=getalfunctie)
knop4.grid(row=2, column=0)

getalfunctie = partial(getal,5)
knop5 = tk.Button(master=venster, text="5", width=5, command=getalfunctie)
knop5.grid(row=2, column=1)

getalfunctie = partial(getal,6)
knop6 = tk.Button(master=venster, text="6", width=5, command=getalfunctie)
knop6.grid(row=2, column=2)

getalfunctie = partial(getal,7)
knop7 = tk.Button(master=venster, text="7", width=5, command=getalfunctie)
knop7.grid(row=3, column=0)

getalfunctie = partial(getal,8)
knop8 = tk.Button(master=venster, text="8", width=5, command=getalfunctie)
knop8.grid(row=3, column=1)

getalfunctie = partial(getal,9)
knop9 = tk.Button(master=venster, text="9", width=5, command=getalfunctie)
knop9.grid(row=3, column=2)

getalfunctie = partial(getal,0)
knop10 = tk.Button(master=venster, text="0", width=5, command=getalfunctie)
knop10.grid(row=4, column=0)

knop11 = tk.Button(master=venster, text="+", width=5)
knop11.grid(row=4, column=1)

knop12 = tk.Button(master=venster, text="-", width=5)
knop12.grid(row=4, column=2)

knop13 = tk.Button(master=venster, text="=", width=5)
knop13.grid(row=5, column=0)

knop14 = tk.Button(master=venster, text="clr", width=12)
knop14.grid(row=5, column=1, columnspan=2)

# Maak de GUI zichtbaar op de computer.
venster.mainloop()