# Maak onderstaande functies af.
# Testen kan MBV de oproepen onder iedere oefeningen.
# Tip: gebruik CTRL + / om meerdere lijnen in/uit commentaar te zetten.

# Deze websites geven meer info over de verschillende methodes van lijsten:
# https://www.w3schools.com/python/python_ref_list.asp
# https://www.programiz.com/python-programming/methods/list

def doorzoek_lijst(lijst, waarde):
    """ return de index van de waarde in de lijst  (index is niet positie!)

        >>> print( doorzoek_lijst([1,4,2,5,9], 9) ) --> 4
    """
    return lijst.index(waarde)

# print( doorzoek_lijst([1,4,2,5,9], 9) )
# print( doorzoek_lijst([1,4,2,5,9], 4) )
# print( doorzoek_lijst([1,4,2,5,9], 5) )

"""
In volgende oefeningen wordt een telefoonboek gebruikt.
Dit telefoonboek ziet er in het begin van iedere oefening als volgt uit.
"""
boek = [
    ["Jan Janssen", "+32 470 998301"],
    ["Piet Joris", "+32 483 313220"],
    ["Kor Neel", "+32 453 231456"]
]

def doorzoek_telefoonboek(boek, persoon):
    """ return het telefoonnummer van de persoon uit het telefoonboek 
    
        boek: lijst van lijsten (geneste lijst), met persoon-nummer paren.
        persoon: naam van de te zoeken persoon.
        Indien de persoon niet in het telefoonnummer staat, return None.

        >>> print( doorzoek_telefoonboek(boek, "Kor Neel") ) --> "+32 453 231456"
    """
    for i in boek:
        naam = i[0]
        if naam == persoon:
            return i[1]

# print( doorzoek_telefoonboek(boek, "Kor Neel") )
# print( doorzoek_telefoonboek(boek, "Jan Janssen") )
# print( doorzoek_telefoonboek(boek, "Piet :Neel") )

def voeg_toe_telefoonboek(boek, persoon, nummer):
    """ return het boek, met de persoon/nummer eraan toegevoegd 
    
        Als persoon-nummer paar reeds in boek staat, voeg niets toe.
        Return in plaats de boodschap "Gegevens reeds in boek".

        Als nummer reeds in gebruik is, voeg niets toe.
        Return in plaats de booschap "Nummer al bezet".

        >>> print( voeg_toe_telefoonboek(boek, "Piet Dirkx", "123") ) -->
            [
                ["Jan Janssen", "+32 470 998301"],
                ["Piet Joris", "+32 483 313220"],
                ["Kor Neel", "+32 453 231456"],
                ["Piet Dirkx", "123]
            ]
    """
    nieuw_nummer = []
    nieuw_nummer.append(persoon)
    nieuw_nummer.append(nummer)

    for nummers in boek:
        if nieuw_nummer != nummers:
            boek.append(nieuw_nummer)
    return boek

# print( voeg_toe_telefoonboek(boek, "Piet Dirkx", "123") )
# print( voeg_toe_telefoonboek(boek, "Piet Joris", "+32 483 313220") )
# print( voeg_toe_telefoonboek(boek, "Jaak Jean" , "+32 470 998301") )

def verwijder_telefoonboek(boek, persoon, nummer): 
    """ return het boek, met bovenstaan persoon-nummer paar verwijderd 
    
        Als persoon-nummer paar niet in boek staat, verwijder niets.
        Return in plaats de boodschap "Gegevens niet aanwezig in boek".

        >>> print( verwijder_telefoonboek(boek, "Piet Joris", "+32 483 313220") ) -->
            [
                ["Jan Janssen", "+32 470 998301"],
                ["Kor Neel", "+32 453 231456"]
            ]
    """
    return None

# print( verwijder_telefoonboek(boek, "Piet Joris"   , "+32 483 313220") )
# print( verwijder_telefoonboek(boek, "Piet Joris"   , "123") )
# print( verwijder_telefoonboek(boek, "Niels Janssen", "+32 470 998301") )

def sorteer_boek(boek):
    """ return het boek, met de paren alfabetisch gesorteerd OBV de persoon
        >>> print( sorteer_boek(boek, True) ) -->
            [
                ["Jan Janssen", "+32 470 998301"],
                ["Kor Neel", "+32 453 231456"],
                ["Piet Joris", "+32 483 313220"]
            ]
        
        Tip: zoek het niet te ver.
    """
    return None

# print( sorteer_boek(boek) )