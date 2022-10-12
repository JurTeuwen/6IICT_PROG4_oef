import csv                                                      # open de module csv

fp = open("hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" )   # open volcanic-eruptions-EU en stop het in variabelen fp
csv_reader = csv.reader( fp , delimiter=";")                    # lees de volcanic-eruptions-EU en deel de woorden op na elke ;

for rij in csv_reader:                                          # haal rij uit csv_reader
    print(rij[1], rij[4])                                                  # print rij

fp.close()                                                      # Na sluiten is CSV niet meer bruikbaar