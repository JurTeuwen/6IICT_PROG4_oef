import csv# importeer module csv

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" ) # open het bestand
csv_reader = csv.DictReader( fp , delimiter=";")#gebruik de functie csv reader om het bestand de lezen als Dict

eruptions_ld = []                                                       # ld = lijst van dictionaries
for dict in csv_reader:                                                 #doorloop de dictionaries van de lezer
    nieuwe_dict = {}                                                    #maak een nieuw dict aan
    for key,value in dict.items():                                      #doorloop iedere key en value in dict met functie items
        if key == "Year":                                               #als de key gelijk is aan "Year"
            value1 = int(value)                                         #maak de value een int
            if value1 < 0:                                              #als de value negatief is
                value2 = str(abs(value1))                               #maak het getal positief en dan weer een string
            else:                                                       #anders
                value2 = value                                          #hou het getal zo
            nieuwe_dict[key]= value                                     #zet het in de nieuwe dict

        if key == "Name":                                               #als de key "Name" is
            kleine_letter = value[0].lower() + value[1:]                #maak de eerste letter een kleine letter en hou de rest zo
            nieuwe_dict[key] = kleine_letter                            #zet het in de nieuwe dict
    eruptions_ld.append(nieuwe_dict)                                    #voeg nieuwe dicht toe aan lijst
fp.close()                                                              # Na sluiten is CSV niet meer bruikbaar

print("")                                                               # print lege lijn
print(eruptions_ld)                                                     #print de lijst
