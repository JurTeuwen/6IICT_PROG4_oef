import csv # importeer de module csv

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" )# open het bestand in read modus
# var csv_reader kan je niet rechtstreeks wijzigen of oproepen.
csv_reader = csv.reader( fp , delimiter=";") #gebruik functie csv 
# reader om het bestand te lezen
# print(csv_reader[3]) # Voorbeeld

# Aanmaken ECHTE lijst van lijsten (ll) en hierin gegevens stoppen
eruptions_ll = []# maak een lege lijst aan
for rij in csv_reader: # doorloop de rijen
    if rij[1] != 'Year':
        jaar = int(rij[1])
        if jaar < 0:
            jaar_correct = str(abs(jaar))
        else:
            jaar_correct = rij[1]
    else:
        jaar_correct = 'Year'
    if rij[4] != 'Name':
        naam = rij[4]
        naam_correct = naam[0].lower() + naam[1:] 
    else:
        naam_correct = 'Name'
    eruptions_ll.append([jaar_correct,naam_correct])# voeg deze rijen toe aan de lege lijst

fp.close() # Na sluiten is CSV niet meer bruikbaar


print(eruptions_ll)#print lijst
