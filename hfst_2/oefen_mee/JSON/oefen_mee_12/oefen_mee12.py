import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/JSON/oefen_mee_12/oefenmee12.json", "r")
dagen = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

dag = input("Welke dag wil je weten: ")
print(dagen[dag])
aanpassen = input("Wil je dit aanpassen: ")
if aanpassen == "ja":
    aanpassing = input(f"Wat ga je doen op {dag}: ")
    dagen[dag] = aanpassing
x = open("hfst_2/oefen_mee/JSON/oefen_mee_12/oefenmee12.json", "w")
json.dump(dagen, x)
x.close()