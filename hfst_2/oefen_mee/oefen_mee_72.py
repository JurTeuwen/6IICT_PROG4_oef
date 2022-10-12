import csv

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" )
csv_reader = csv.DictReader( fp , delimiter=";")

eruptions_ld = [] # ld = lijst van dictionaries
for rij in csv_reader:
    eruptions_ld.append(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar



eruptions_ld_verwerkt = []

for index, rij in enumerate(eruptions_ld):
    dict = {}
    dict["Year"] = abs(int(rij["Year"]))
    dict["Name"] = rij["Name"].lower()
    eruptions_ld_verwerkt.append(dict)

fp = open( "eruptions_ld_verwerkt.csv", "w", newline="" )#je opend/maakt een bestand gemaakt "kritieken_to_csv.csv"
csv_writer = csv.DictWriter( fp , delimiter=";", fieldnames=["Year", "Name"])#maak variabelen aan om lijst van dicts wag te schrijven

csv_writer.writeheader()#schrijf de header
for rij in eruptions_ld_verwerkt:#overloop elke rij in film_kritieken
    csv_writer.writerow(rij)#schrijf elke rij

fp.close() # Na sluiten is CSV niet meer bruikbaar
