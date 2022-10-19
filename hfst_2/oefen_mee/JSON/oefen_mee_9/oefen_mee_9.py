import json
goed = 0
fout = 0
# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/JSON/oefen_mee_9/oefenmee9.json", "r")
quiz = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

for hoofding, themas in quiz.items():
    for thema, aantal_vragen in themas.items():
        print("")
        print(thema)
        for aantal_vraag, vraag in aantal_vragen.items():
            print("")
            print(aantal_vraag)
            for key, info in vraag.items():
                if key == "antwoord":
                    antwoord = input(f"Wat is je antwoord: ")
                    if antwoord == info:
                        print("Goed bezig, je antwoord was goed")
                        goed = goed+1
                    else:
                        print(f"Jammer, {antwoord} is niet goed. Het juiste antwoord was {info}")
                        fout = fout+1
                else:
                    print(f"{key}:{info}")
totaal = goed+fout
print("")
print(f"Je uiteindelijke score is {goed} op {totaal}")