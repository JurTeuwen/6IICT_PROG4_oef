import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/JSON/oefen_mee_8/oefenmee8.json", "r")
dagen = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar


dag = input("Welke dag wil je weten: ")
print(dagen[dag])
