import csv

film_kritieken = [                                              #lijst van dictionaries 
    {"FILM": "Monty Python and the Holy Grail", "SCORE": 8},
    {"FILM": "Monty Python's Life of Brian", "SCORE": 8.5},
    {"FILM": "Monty Python's Meaning of Life", "SCORE": 7}
]
film_header = ["FILM", "SCORE"]

fp = open( "kritieken_to_csv.csv", "w", newline="" )#je opend/maakt een bestand gemaakt "kritieken_to_csv.csv"
csv_writer = csv.DictWriter( fp , delimiter=";", fieldnames=film_header)#maak variabelen aan om lijst van dicts wag te schrijven

csv_writer.writeheader()#schrijf de header
for rij in film_kritieken:#overloop elke rij in film_kritieken
    csv_writer.writerow(rij)#schrijf elke rij

fp.close() # Na sluiten is CSV niet meer bruikbaar
