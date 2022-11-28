""" Niveau 1 """
try:
    num_lijst = [ 100, 101, 0, "103", 104 ]
    index = int( input( "Geef een index: " ) )

except ValueError:
    print("je kan geen getal of symbool ingeven")

else:
    try:
        print( f"100 / {num_lijst[index]} = {100/num_lijst[index]}" )
    except ZeroDivisionError:
        print("dit is niet mogelijk")
    except TypeError:
        print("dit is niet mogelijk")
    except IndexError:
        print("Zoveel getallen staat niet in de lijst")


finally:
    print( "Geldig getal als index opgegeven." )