""" 
Voorbeeld:

>>> input() = "Dit is een zin"
>>> Dict    = {"Dit": "tiD", "is": "si", "een": "nee", "zin": "niz"}

Tip: je hebt al in de reeksen gezien hoe een woord om te keren.
"""

zin = input("Geef een zin op: ")
dictonary = {}
zin_in_lijst = zin.split()
for woord in zin_in_lijst:
    omgekeerd_woord = woord[::-1 ]
    dictonary[woord] = omgekeerd_woord
print(dictonary)