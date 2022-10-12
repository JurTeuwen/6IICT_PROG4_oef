import csv

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" )
csv_reader = csv.DictReader( fp , delimiter=";")

eruptions_ld = [] # ld = lijst van dictionaries
for rij in csv_reader:
    print(rij)
    eruptions_ld.append(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar

print("")
# print(eruptions_ld)


eruptions_ld_verwerkt = []

for index, rij in enumerate(eruptions_ld):
    dict = {}
    dict["Year"] = abs(int(rij["Year"]))
    dict["Name"] = rij["Name"].lower()
    eruptions_ld_verwerkt.append(dict)

print(eruptions_ld_verwerkt)