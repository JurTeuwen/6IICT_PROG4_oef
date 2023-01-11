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
    link_1.delete(0, 1) # delete het linkse letter

    web_2 = link_2.get()    # haal de info uit invulvlak en stop het in variabelen web_2
    link_2.delete( 0, web_2.find(".")+1 )   # zoek de index van de ., tel daar 1 bij op. Vanaf het begin tot die index verwijder je

knop = tk.Button(master=venster, command=reset_links,   # maak een nieuwe knop aan met als command de functie genaamd reset_links
                 text="Reset input!", width=50)
knop.grid(row=2, column=0, columnspan=2)    # voeg de knop toe aan het venster op plaats 2,0 met en columnspan van 2

venster.mainloop()  # laat het venster zien