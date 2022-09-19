import time
from random import randrange
grootte = 100 # Nummer zelf te kiezen (kies groter dan 99)

zoek_getal = randrange(grootte, grootte*2) # Genereer een te zoeken getal

""" ------------------------LIJST--------------------------  """
lijst = []
for i in range(grootte*2): 
    lijst.append(i)

start = time.perf_counter()
if zoek_getal in lijst:
    print(zoek_getal)
print(f"{time.perf_counter()-start} seconden nodig om getal in lijst te vinden.")

""" ---------------------DICTIONARY-----------------------  """
dict = {}
for i in range(grootte*2):
    dict[i] = i

start = time.perf_counter()
if zoek_getal in dict: # Je kan "in" ook gebruiken om een specifieke key te zoeken.
    print(zoek_getal)
print(f"{time.perf_counter()-start} seconden nodig om getal in dict te vinden.")
