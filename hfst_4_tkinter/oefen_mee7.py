import tkinter as tk    # import de library tkinter als tk

venster = tk.Tk()   # maak een nieuw venster aan

label = tk.Label(master=venster, text="Geef naam op: ", width=15, height=2,     # maak een label aan
                 highlightthickness=2, highlightbackground="black")
label.grid(row=0, column=0) # voeg de label toe aan het venster op plaats 0,0

veld = tk.Entry(master=venster, width=50, fg="red") # maak een invulveld aan
veld.grid(row=0, column=1)  # voeg het invulveld toe aan het venster op plaats 0,1

def display_naam(): # maak een defenitie aangenaamt display_naam
    tekst = f"Hallo, mijn naam is {veld.get()}!"    # haal de informatie uit het invulveld en stop het in een zin. Stop die zin in variabelen tekst
    label_naam = tk.Label(master=venster, text=tekst, width=50, height=2)   # maak een nieuwe label aan
    label_naam.grid(row=2, column=0, columnspan=2)  # voeg de label toe aan het venster op plaat 2,0 met een columnspan van 2

knop = tk.Button(master=venster, command=display_naam, text="Voer in!", width=50)   # maak een nieuwe knop aan met als command de functie display_naam
knop.grid(row=1, column=0, columnspan=2)    # voeg de knop toe aan het venster op plaat 1,0 met een columnspan van 2

venster.mainloop()  # laat het venster zien
