fruit_lijst = ["Appel", "Banaan", "Kers"]
try:
    getal = input( "Geef een getal: " )
    if "." in getal:
        getal = float( getal )
    else:
        getal = int( getal )
    print( fruit_lijst[getal] )
except IndexError:
    print("Zoveel fruit staat niet in de lijst")
except ValueError:
    print("je kan geen getal of symbool ingeven")
except TypeError:
    print("je kan geen commagetal ingeven")

print("Programma klaar")  
