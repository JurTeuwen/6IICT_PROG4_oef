import csv

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" )
# var csv_reader kan je niet rechtstreeks wijzigen of oproepen.
csv_reader = csv.reader( fp , delimiter=";") 
# print(csv_reader[3]) # Voorbeeld

# Aanmaken ECHTE lijst van lijsten (ll) en hierin gegevens stoppen
eruptions_ll = []
for rij in csv_reader:
    eruptions_ll.append(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar

print("")
print(eruptions_ll)


eruptions_ll_verwerkt = []

for index, rij in enumerate(eruptions_ll):
    if index == 0:
        eruptions_ll_verwerkt.append((rij[1], rij[4]))
    else:
        eruptions_ll_verwerkt.append((abs(int(rij[1])), rij[4].lower()))

print(eruptions_ll_verwerkt)