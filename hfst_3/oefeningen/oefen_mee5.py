""" Niveau 1 & 2
Wat gaat hier mis?
"""
fruit_lijst = ["Appel", "Banaan", "Meloen", "Mango", "Druif"]
try:
    getal = int( input("Hoeveel fruit uit de lijst wil je printen: ") )

    for i in range(getal):
        fruit = fruit_lijst[i]
        print(fruit)
except IndexError:
    print("Zoveel fruit staat niet in de lijst")
except ValueError:
    print("je kan geen getal of symbool ingeven")


""" Niveau 3 (haal uit commentaar) """
while True:
    fruit = input("Element aan lijst toevoegen: ")
    
    if fruit == "":
        break # Loop stopt wanneer gebruiker een lege string ingeeft.
    else:
        fruit_lijst.append(fruit)

print(fruit_lijst)
