import tkinter as tk    # import de library tkinter als tk

venster = tk.Tk()   # maak een nieuw venster aan

label = tk.Label(master=venster, text="Welke website wil je bezoeken?", height=2)   # maak een nieuw label aan
label.grid(row=0, column=0, columnspan=2)   # voeg de label toe aan het venster met een columnspan van 2

link_1 = tk.Entry(master=venster, width=33, font=("Helvetica",14),  # maak een nieuw invulvlak
                  border=10, borderwidth=5)
link_1.grid(row=1, column=0)    # voeg het invulvlak toe aan het venster op plaats 1,0

link_2 = tk.Entry(master=venster, width=33, font=("Helvetica",14),  # maak een nieuw invulvlak
                  border=10, borderwidth=5)
link_2.grid(row=1, column=1)    # voeg het invulvlak toe aan het venster op plaats 1,1

def reset_links():  # maak een defenitie aan genaamd reset_links
    link_1.delete(0, tk.END) # delete alles
    link_1.insert(0, "www.")    # insert www. in het invulvlak

    link_2.insert( tk.END, ".com" )   # insert .com op het laatste in het invulvlak

knop = tk.Button(master=venster, command=reset_links,   # maak een nieuwe knop aan met als command de functie genaamd reset_links
                 text="Reset input!", width=50)
knop.grid(row=2, column=0, columnspan=2)    # voeg de knop toe aan het venster op plaats 2,0 met en columnspan van 2

venster.mainloop()  # laat het venster zien