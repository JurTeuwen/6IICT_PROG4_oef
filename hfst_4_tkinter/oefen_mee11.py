# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Maak een lege GUI aan.
venster = tk.Tk()


veld = tk.Entry(master=venster, font=("Helvetica",14), border=10, borderwidth=5)
veld.grid(row=0, column=0)

# TODO: functie aanmaken gelinkt aan Button knop.
#       Doel van functie is toevoegen van Entry veld aan Label onder de knop.
def toevoegen():
    global zin
    woord = veld.get()
    zin = zin + woord
    label = tk.Label(master=venster, text=zin)
    label.grid(row=2, column=0)
    veld.delete(0, tk.END)
zin = ""
knop = tk.Button(master=venster, command=toevoegen, text="Voeg toe aan string:", width=50)
knop.grid(row=1, column=0, pady=10, padx= 10)

# Maak de GUI zichtbaar op de computer.
venster.mainloop()