# Maak onderstaande functies af.
# Testen kan MBV de oproepen onder iedere oefeningen.
# Tip: gebruik CTRL + / om meerdere lijnen in/uit commentaar te zetten.

def voeg_toe(x,y):
    """ return de som van x en y """
    return x+y

# print( voeg_toe(3,5) )
# print( voeg_toe(2,9) )
# print( voeg_toe(-3,5) )

def kwadraat(x):
    """ return het kwadraat van x """
    return x**2

# print( kwadraat(3) )
# print( kwadraat(8) )
# print( kwadraat(-1) )

def oppervlakte_kubus(x):
    """ print de oppervlake van een kubus met zijde z """
    return x*x*6

# print(oppervlakte_kubus(4))
# print(oppervlakte_kubus(1))
# print(oppervlakte_kubus(5))

def seconden_per_dag(dagen=1):
    """ return het aantal seconden in het opgegeven aantal dagen
         
        Indien de oproep zonder argument gebeurt, geef het aantal
        seconden in 1 dag terug. Gebruik een "default value".
    """
    return dagen*24*60*60

# print( seconden_per_dag(3) )
# print( seconden_per_dag( ) )
# print( seconden_per_dag(7) )

def seconden_per_jaar(jaren):
    """ return het aantal seconden in het opgegeven aantal jaren 
    
        Veronderstel dat ieder jaar uit exact 52 weken bestaat.  
    """
    return jaren*52*7*24*60*60

# print( seconden_per_jaar(4) )
# print( seconden_per_jaar(1) )
# print( seconden_per_jaar(0) )

def seconden_in_leven(leeftijd, is_man = False):
    """ return het aantal seconden die een persoon nog heeft 
    
        Veronderstel dat een man maximaal 80 jaar leeft,
                    en een vrouw maximaal 84 jaar leeft.

        Maak gebruik van seconden_per_jaar.
    """
    if is_man == True:
        jaren_tot_dood=80-leeftijd
    else:
        jaren_tot_dood=84-leeftijd
    return seconden_per_jaar(jaren_tot_dood)

# print( seconden_in_leven(0, True) )
# print( seconden_in_leven(74, False) )
# print( seconden_in_leven(56) )


