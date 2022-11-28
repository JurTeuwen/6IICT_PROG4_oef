import csv                                                              # importeer libraries
import matplotlib.pyplot as plt
bladeren=["geen", "rood", "oranje", "geel", "groen", "blauw"]           # alle kleuren in een lijst
lijst_y_zwarte_achtergrond = []                                         # nieuwe lijst met y-waarden
lijst_y_witte_achtergrond = []                                          # nieuwe lijst met y-waarden

# Waarden 1ste grafiek in een lijst zetten
for blad in bladeren:                                                   # overloop de kleuren in de lijst bladeren
    fp = open(f"hfst_2/taak/zwarte achtergrond/{blad} blad.csv", "r" )  # open de info en stop het in variabelen fp
    csv_reader = csv.reader( fp , delimiter=",")                        # lees de fp en deel de woorden op na elke ,
    waarden = []                                                        # nieuwe lijst voor waarden
    for rij in csv_reader:                                              # haal rij uit csv_reader
        waarden.append(rij[1])                                          # stop de laatste waarden in de lijst
    del waarden[0]                                                      # delete de eerste waarde
    gemiddelde = []                                                     # nieuwe lijst voor het berekenen van gemiddelde
    for waarde in waarden:                                              # overloop de lijst waarden
        gemiddelde.append(float(waarde))                                # voeg de float van de waarde toe aan de lijst
    y_coordinaat = sum(gemiddelde)/len(gemiddelde)                      # bereken het gemiddelde
    lijst_y_zwarte_achtergrond.append(y_coordinaat)                     # zet gemiddelde in een lijst

# Waarden 2de grafiek in een lijst zetten
for blad in bladeren:                                                   # overloop de kleuren in de lijst bladeren
    fp = open(f"hfst_2/taak/witte achtergrond/{blad} blad.csv", "r" )   # open de info en stop het in variabelen fp
    csv_reader = csv.reader( fp , delimiter=",")                        # lees de fp en deel de woorden op na elke ,
    waarden = []                                                        # nieuwe lijst voor waarden
    for rij in csv_reader:                                              # haal rij uit csv_reader
        waarden.append(rij[1])                                          # stop de laatste waarden in de lijst
    del waarden[0]                                                      # delete de eerste waarde
    gemiddelde = []                                                     # nieuwe lijst voor het berekenen van gemiddelde
    for waarde in waarden:                                              # overloop de lijst waarden
        gemiddelde.append(float(waarde))                                # voeg de float van de waarde toe aan de lijst
    y_coordinaat = sum(gemiddelde)/len(gemiddelde)                      # bereken het gemiddelde
    lijst_y_witte_achtergrond.append(y_coordinaat)                      # zet gemiddelde in een lijst

fp.close()                                                              # Na sluiten is CSV niet meer bruikbaar

# Maak de linkse staafdiagram.
plt.subplot(1,2,1)  
plt.bar(1, lijst_y_zwarte_achtergrond[0], width=0.8, align='center', color='black', label="geen blad")
plt.bar(2, lijst_y_zwarte_achtergrond[1], width=0.8, align='center', color='red', label="rood blad")
plt.bar(3, lijst_y_zwarte_achtergrond[2], width=0.8, align='center', color='orange', label="oranje blad")
plt.bar(4, lijst_y_zwarte_achtergrond[3], width=0.8, align='center', color='yellow', label="geel blad")
plt.bar(5, lijst_y_zwarte_achtergrond[4], width=0.8, align='center', color='green', label="groen blad")
plt.bar(6, lijst_y_zwarte_achtergrond[5], width=0.8, align='center', color='blue', label="blauw blad")
plt.title("lichtproef met zwarte achtergrond")
plt.legend()
plt.xlabel("experimentnummer")
plt.ylabel("luminantie in lux")

# Maak de rechtse staafdiagram
plt.subplot(1,2,2)
plt.bar(1, lijst_y_witte_achtergrond[0], width=0.8, align='center', color='black', label="geen blad")
plt.bar(2, lijst_y_witte_achtergrond[1], width=0.8, align='center', color='red', label="rood blad")
plt.bar(3, lijst_y_witte_achtergrond[2], width=0.8, align='center', color='orange', label="oranje blad")
plt.bar(4, lijst_y_witte_achtergrond[3], width=0.8, align='center', color='yellow', label="geel blad")
plt.bar(5, lijst_y_witte_achtergrond[4], width=0.8, align='center', color='green', label="groen blad")
plt.bar(6, lijst_y_witte_achtergrond[5], width=0.8, align='center', color='blue', label="blauw blad")
plt.title("lichtproef met witte achtergrond")
plt.legend()
plt.xlabel("experimentnummer")
plt.ylabel("luminantie in lux")

plt.show()