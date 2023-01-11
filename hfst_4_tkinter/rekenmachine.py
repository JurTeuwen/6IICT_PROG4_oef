# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Maak een lege GUI aan.
venster = tk.Tk()

# Label aanmaken.
    # master: geef aan tot welke GUI het label behoort.
    # text: boodschap van het label.
veld = tk.Entry(master=venster, bg="green")  # maak een nieuw invulvlak
veld.grid(row=0, column=0, columnspan=3)

knop1 = tk.Button(master=venster, text="1", width=5)
knop1.grid(row=1, column=0)

knop2 = tk.Button(master=venster, text="2", width=5)
knop2.grid(row=1, column=1)

knop3 = tk.Button(master=venster, text="3", width=5)
knop3.grid(row=1, column=2)

knop4 = tk.Button(master=venster, text="4", width=5)
knop4.grid(row=2, column=0)

knop5 = tk.Button(master=venster, text="5", width=5)
knop5.grid(row=2, column=1)

knop6 = tk.Button(master=venster, text="6", width=5)
knop6.grid(row=2, column=2)

knop7 = tk.Button(master=venster, text="7", width=5)
knop7.grid(row=3, column=0)

knop8 = tk.Button(master=venster, text="8", width=5)
knop8.grid(row=3, column=1)

knop9 = tk.Button(master=venster, text="9", width=5)
knop9.grid(row=3, column=2)

knop10 = tk.Button(master=venster, text="0", width=5)
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
