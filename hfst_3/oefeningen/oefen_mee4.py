woord = input("Geef een woord op: ")
if len(woord) < 5:
    klein_woord = True

try:
    print(f"Huidige waarde klein_woord: {klein_woord}")
except NameError:
    if len(woord) >= 5:
        klein_woord = False

if klein_woord:
    print(f"{woord} is een klein woord")
else:
    print(f"{woord} is een groot woord")
