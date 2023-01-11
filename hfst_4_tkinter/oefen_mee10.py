# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Vraag om de lievelingskleur van de gebruiker (rood, groen of blauw)
kleur = input("Wat is je favoriete kleur? ")

# Maak een lege GUI aan.
venster = tk.Tk()

# TODO: vertaal input van gebruiker naar het Engels
def Engels_Kleur():
    global kleur
    if kleur == 'groen':
        kleur = 'green'
    if kleur == 'rood':
        kleur = 'red'
    if kleur == 'blauw':
        kleur = 'blue'
# TODO: maak functie aan die het label in de ingegeven kleur laat zien.
def kleur_label():
    global kleur
    Engels_Kleur()
    veld = tk.Entry(master=venster, width=33, bg=kleur)
    veld.grid(row=1, column=0)
    veld.insert(0, kleur)

knop = tk.Button(master=venster, text="Klik op mij!", command= kleur_label)
knop.grid(row=0, column=0)

# Maak de GUI zichtbaar op de computer.
venster.mainloop()