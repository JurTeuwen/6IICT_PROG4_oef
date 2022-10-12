import csv# open de module csv

fp = open( "volcanic-eruptions-EU.csv", "r" )# open volcanic-eruptions-EU en stop het in variabelen fp
# var csv_reader kan je niet rechtstreeks wijzigen of oproepen.
csv_reader = csv.reader( fp , delimiter=";") # lees de volcanic-eruptions-EU en deel de woorden op na elke ;
# print(csv_reader[3]) # Voorbeeld

# Aanmaken ECHTE lijst van lijsten (ll) en hierin gegevens stoppen
eruptions_ll = []#maak een lege lijst aan
for rij in csv_reader:#doorloop alle rijen in csv_reader
    eruptions_ll.append(rij)#voeg de rijen toe aan de lijst

fp.close() # Na sluiten is CSV niet meer bruikbaar

for eruption in eruptions_ll:
    print(eruption)



fp = open("hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" )
csv_reader = csv.DictReader( fp , delimiter=";")

eruptions_ld = [] # ld = lijst van dictionaries
for rij in csv_reader:
    print(rij)
    eruptions_ld.append(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar

print("")
print(eruptions_ld)
