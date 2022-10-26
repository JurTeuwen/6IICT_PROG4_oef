import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/JSON/oefen_mee_13/oefenmee13.json", "r")
informatie = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

besmettingen = []
for dagen in informatie:
    besmettingen.append(dagen['Cases'])
    for index,aantal in enumerate(besmettingen):
        if index > 0:
            nieuwe_besmettingen = besmettingen[-1]-besmettingen[-2]
        else:
            nieuwe_besmettingen= 0
    print(f"{dagen['Date']} waren er {nieuwe_besmettingen} nieuwe besmettingen")
    dagen["nieuwe_besmettingen"] = nieuwe_besmettingen

fp = open("hfst_2/oefen_mee/JSON/oefen_mee_13/oefenmee13.json", "w")
json.dump(informatie, fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar