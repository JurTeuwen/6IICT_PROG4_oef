import csv                                                          # importeer libraries
import matplotlib.pyplot as plt
bladeren=["geen", "rood", "oranje", "geel", "groen", "blauw"]       # alle kleuren in een lijst
lijst_y = []                                                        # nieuwe lijst met y-waarden
for blad in bladeren:                                               # overloop de kleuren in de lijst bladeren
    fp = open(f"hfst_2/taak/{blad} blad.csv", "r" )                 # open de info en stop het in variabelen fp
    csv_reader = csv.reader( fp , delimiter=",")                    # lees de fp en deel de woorden op na elke ,
    waarden = []                                                    # nieuwe lijst voor waarden
    for rij in csv_reader:                                          # haal rij uit csv_reader
        waarden.append(rij[1])                                      # stop de laatste waarden in de lijst
    del waarden[0]                                                  # delete de eerste waarde
    gemiddelde = []                                                 # nieuwe lijst voor het berekenen van gemiddelde
    for waarde in waarden:                                          # overloop de lijst waarden
        gemiddelde.append(float(waarde))                            # voeg de float van de waarde toe aan de lijst
    y_coordinaat = sum(gemiddelde)/len(gemiddelde)                  # bereken het gemiddelde
    lijst_y.append(y_coordinaat)                                    # zet gemiddelde in een lijst

fp.close()                                                          # Na sluiten is CSV niet meer bruikbaar

# maak de staafdiagram
plt.bar(1, lijst_y[0], width=0.8, align='center', color='black', label="geen blad")
plt.bar(2, lijst_y[1], width=0.8, align='center', color='red', label="rood blad")
plt.bar(3, lijst_y[2], width=0.8, align='center', color='orange', label="oranje blad")
plt.bar(4, lijst_y[3], width=0.8, align='center', color='yellow', label="geel blad")
plt.bar(5, lijst_y[4], width=0.8, align='center', color='green', label="groen blad")
plt.bar(6, lijst_y[5], width=0.8, align='center', color='blue', label="blauw blad")

plt.title("lichtproef")
plt.legend()
plt.xlabel("experimentnummer")
plt.ylabel("luminantie in lux")

plt.show()