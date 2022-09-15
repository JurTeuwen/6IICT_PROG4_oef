# Maak onderstaande functies af.
# Testen kan MBV de oproepen onder iedere oefeningen.
# Tip: gebruik CTRL + / om meerdere lijnen in/uit commentaar te zetten.



from cmath import pi
from math import floor


def grootste(x,y,z):
    """ return het grootste van de drie getallen """
    return max(x, y, z)

# print( grootste(1,2,3) )
# print( grootste(9,6,3) )
# print( grootste(3,7,5) )

def grootste_lijst(lijst):
    """ return het grootste getal uit een lijst van getallen """
    return max(lijst)

# print( grootste_lijst([2, 6, 8, 23, 12, 2]) )
# print( grootste_lijst([4, 6, -3, 10, 5, 3]) )
# print( grootste_lijst([1, 3, 2]) )

def temperatuur_voorspelling(temp):
    """ return een boodschap afhankelijk van de temperatuur 
        
        temp < 0:       Het vriest bij "temp" graden.
        0 < temp < 10:  Het is koud bij "temp" graden.
        10 < temp < 20: Het is fris bij "temp" graden.
        20 < temp < 30: Het is normaal bij "temp" graden.
        30 < temp:      Het is heet bij "temp" graden.

        Maak gebruik van f-strings om de boodschap op te stellen. 
    """
    if temp < 0:
        return f"Het vriest bij {temp} graden."
    if temp < 10:
        return f"Het is koud bij {temp} graden."
    if temp < 20:
        return f"Het is fris bij {temp} graden."
    if temp < 30:
        return f"Het is normaal bij {temp} graden."
    if temp > 30:
        return f"Het is heet bij {temp} graden."

# print( temperatuur_voorspelling(-3) )
# print( temperatuur_voorspelling(8) )
# print( temperatuur_voorspelling(44) )

def temperatuur_conversie():
    """ print de boodschap van temperatuur_voorspelling 
    
        Gebruiker geeft als INPUT de temperatuur in Fahrenheit.
        Converteer deze temperatuur naar Celsius en print met deze
        waarde de boodschap van temperatuur voorspelling. 

        Tip: denk goed na over het datatype van je variabelen.
    """
    Fahrenheit= int(input("Temperatuur in Fahrenheit"))
    Celsius = (Fahrenheit-32)/1.8
    return Celsius

# print(temperatuur_conversie())

def berekeningen(x,y):
    """ return zowel de som als het verschil van x en y 
    
        >>> print( berekeningen(10,40) ) --> (50, -30)
    """
    som = x+y
    verschil = x-y
    return som, verschil

# print( berekeningen(10, 40) )
# print( berekeningen(4, 44) )
# print( berekeningen(60, 30))

def omtrek(straal):
    """ return de omtrek van een cirkel, afgerond naar beneden 
    
        Formule: A = 2 * pi * straal

        De functie moet ook werken met een negatief getal als argument.
        Maak in dit geval het getal positief.
    """
    A = floor(2*pi*straal)
    return A

print( omtrek(4) )
print( omtrek(-8) )
print( omtrek(2) )
    
