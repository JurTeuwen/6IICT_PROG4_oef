# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# 2 getallen vragen aan gebruiker.
getal_1 = int(input("Getal 1: "))
getal_2 = int(input("Getal 2: "))

# Maak een lege GUI aan.
venster = tk.Tk()

# TODO: functie aanmaken gelinkt aan Button knop.
#       Doel van functie is optellen van ingegeven getallen en plaatsen in een label.
#       Niveau 2: iedere keer als de knop wordt ingeduwd, verhoogt de waarde van dit label.
def optellen():
    global getal_1
    global getal_2
    global resultaat
    som_getal = getal_1+getal_2
    resultaat = resultaat+som_getal
    label = tk.Label(master=venster, text=resultaat)
    label.grid(row=3, column=0, columnspan= 2)
resultaat = 0
# Labels aanmaken en plaatsen.
label = tk.Label(master=venster, text="Geef twee getallen in:", height=2, width=50)
label.grid(row=0, column=0, columnspan=2, pady=2)
label_1 = tk.Label(master=venster, font=("Helvetica",14), border=10, borderwidth=5, text=f"Getal 1: {getal_1}")
label_1.grid(row=1, column=0, padx=10)
label_2 = tk.Label(master=venster, font=("Helvetica",14), border=10, borderwidth=5, text=f"Getal 2: {getal_2}")
label_2.grid(row=1, column=1, padx=10)

# Knop voor tonen resultaat.
knop = tk.Button(master=venster,command=optellen , text="Bereken resultaat:", width=50)
knop.grid(row=2, column=0, columnspan=2, pady=10)


# Maak de GUI zichtbaar op de computer.
venster.mainloop()