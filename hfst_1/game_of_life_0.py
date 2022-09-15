# Maak Conway's Game of Life na. https://www.youtube.com/watch?v=C2vgICfQawE
 
# Stap-1: maak een venv aan, installeer hierin pygame.
# Stap-2: los alle functies op. Controleer zelf of deze functies werken.
# Stap-3: Als alle oproepen correct zijn, haal de onderste twee regels uit commentaar.
#         Je kan nu het programma uitvoeren.  
import copy
import random
import pygame

# De grootte van het speelveld, in aantal cellen.
#
# Met BREEDTE = 3 en HOOGTE = 3, kan een speelveld
# er als volgt uit zien.
# [
#    [0,0,1],
#    [0,1,1],
#    [0,0,1],
# ]

# Het staat je vrij om deze aan te passen.
HOOGTE = 120
BREEDTE = 120

# De breedte en hoogte van iedere cel in pixels. Je mag deze aanpassen.
CEL_HOOGTE = 5
CEL_BREEDTE = 5

# De kans die een dode cel heeft om levend te worden in het begin. Je mag deze aanpassen.
KANS_LEVEND = 0.1

def maak_rij_nul(breedte):
    """ return een lijst gevuld met nullen van de gegeven breedte
    
        breedte: het aantal nullen in een lijst

        >>> print( maak_rij_nul(3) ) --> [0, 0, 0]
    """
    lijst_maak_rij_nul = []
    for i in range(breedte):
        lijst_maak_rij_nul.append(0)
    return lijst_maak_rij_nul


def maak_veld_nul(hoogte, breedte):
    """ return een geneste lijst met grootte: hoogte x breedte

        hoogte: het aantal lege lijsten dat gemaakt moet worden.
        breedte: het aantal nullen in iedere lege lijst.

        >>> print( maak_veld_nul(2,3) ) --> [
                                             [0, 0, 0],
                                             [0, 0, 0]
                                            ]

        Tip: Maak de geneste lijst door maal_rij_nul op te roepen.
             Het aantal oproepen is gelijk aan de waarde van hoogte.
             Zie ook reeks_4 voor het invoegen van een lijst in een lijst.
    """
    veld = []
    for aantal in range(hoogte):
        veld.append(maak_rij_nul(breedte))
    return veld

def maak_veld_nul_levend(veld, kans_levend):
    """ return een veld, waarbij een aantal van de cellen een waarde 1 bevatten 
    
        veld: het veld bekomen uit maak_veld_nul.
        kans_levend: de kans (tussen 0 en 1) die een cel heeft om waarde 1 te krijgen.

        Overloop alle cellen in de geneste lijst. Een aantal van deze cellen moet 
        waarde 1 krijgen. Om te bepalen welke gebruik je kans_levend en de random module.

        veld = [
                [0, 0, 0],
                [0, 0, 0]
               ]

        >>> print( maak_veld_nul_levend(veld, 1  ) ) --> [
                                                          [1, 1, 1],
                                                          [1, 1, 1]
                                                         ]
        >>> print( maak_veld_nul_levend(veld, 0.5) ) --> [
                                                          [1, 0, 1],
                                                          [0, 0, 1]
                                                         ]
    """
    for lijst in veld:
        for i in range(len(lijst)):
            getal = random.random()
            if getal <= kans_levend:
                del lijst[i]
                lijst.insert(i, 1)
    return veld
                


def get_links(veld, y, x):
    """ return de waarde van de cel links van de huidige cel 
   
        y: de y-positie van de huidige cel.
        x: de x-positie van de huidige cel.
        
        Als de huidige cel zich op de linkergrens bevindt, return 0.

        veld = [
            [1, 2],
            [3, 4]
        ]

        >>> print( get_links(veld, 1, 1) ) --> 3
        >>> print( get_links(veld, 0, 1) ) --> 1
        >>> print( get_links(veld, 1, 0) ) --> 0
    """
    rij = veld[y]
    if x == 0:
        return 0
    else:
        return rij[x-1]


def get_rechts(veld, y, x):
    """ return de waarde van de cel rechts van de huidige cel 
   
        y: de y-positie van de huidige cel.
        x: de x-positie van de huidige cel.
        
        Als de huidige cel zich op de rechtergrens bevindt, return 0.

        veld = [
            [1, 2],
            [3, 4]
        ]

        >>> print( get_rechts(veld, 1, 1) ) --> 0
        >>> print( get_rechts(veld, 0, 1) ) --> 0
        >>> print( get_rechts(veld, 1, 0) ) --> 4
    """
    rij = veld[y]
    if x == len(rij)-1:
        return 0
    else:
        return rij[x+1]

def get_boven(veld, y, x):
    """ return de waarde van de cel boven de huidige cel 
        
        y: de y-positie van de huidige cel.
        x: de x-positie van de huidige cel.
        
        Als de huidige cel zich op de bovengrens bevindt, return 0.

        veld = [
            [1, 2],
            [3, 4]
        ]

        >>> print( get_boven(veld, 1, 1) ) --> 2
        >>> print( get_boven(veld, 0, 1) ) --> 0
        >>> print( get_boven(veld, 1, 0) ) --> 1
    """
    if y==0:
        return 0
    else:
        rij = veld[y-1]
        return rij[x]


def get_onder(veld, y, x):
    """ return de waarde van de cel onder de huidige cel 
   
        y: de y-positie van de huidige cel.
        x: de x-positie van de huidige cel.
        
        Als de huidige cel zich op de ondergrens bevindt, return 0.

        veld = [
            [1, 2],
            [3, 4]
        ]

        >>> print( get_onder(veld, 1, 1) ) --> 0
        >>> print( get_onder(veld, 0, 1) ) --> 4
        >>> print( get_onder(veld, 1, 0) ) --> 0
    """
    if y==len(veld)-1:
        return 0
    else:
        rij = veld[y+1]
        return rij[x]


def get_linksboven(veld, y, x):
    """ return de waarde van de cel linksboven de huidige cel 
   
        y: de y-positie van de huidige cel.
        x: de x-positie van de huidige cel.
        
        Als de huidige cel zich op de linkergrens bevindt, return 0.
        Als de huidige cel zich op de bovengrens bevindt, return 0.
        
        veld = [
            [1, 2],
            [3, 4]
        ]

        >>> print( get_linksboven(veld, 1, 1) ) --> 1
        >>> print( get_linksboven(veld, 0, 1) ) --> 0
        >>> print( get_linksboven(veld, 1, 0) ) --> 0
    """
    if y==0 or x==0:
        return 0
    else:
        rij = veld[y-1]
        return rij[x-1]


def get_rechtsboven(veld, y, x):
    """ return de waarde van de cel rechtsboven de huidige cel 
   
        y: de y-positie van de huidige cel.
        x: de x-positie van de huidige cel.
        
        Als de huidige cel zich op de rechtergrens bevindt, return 0.
        Als de huidige cel zich op de bovengrens bevindt, return 0.

        veld = [
            [1, 2],
            [3, 4]
        ]

        >>> print( get_rechtsboven(veld, 1, 1) ) --> 0
        >>> print( get_rechtsboven(veld, 0, 1) ) --> 0
        >>> print( get_rechtsboven(veld, 1, 0) ) --> 2
    """
    rij = veld[y]
    if y==0 or x==len(rij)-1:
        return 0
    else:
        rij = veld[y-1]
        return rij[x+1]

def get_linksonder(veld, y, x):
    """ return de waarde van de cel linksonder de huidige cel 
   
        y: de y-positie van de huidige cel.
        x: de x-positie van de huidige cel.
        
        Als de huidige cel zich op de linkergrens bevindt, return 0.
        Als de huidige cel zich op de ondergrens bevindt, return 0.

        veld = [
            [1, 2],
            [3, 4]
        ]

        >>> print( get_linksonder(veld, 1, 1) ) --> 0
        >>> print( get_linksonder(veld, 0, 1) ) --> 3
        >>> print( get_linksonder(veld, 1, 0) ) --> 0
    """
    if y==len(veld)-1 or x==0:
        return 0
    else:
        rij = veld[y+1]
        return rij[x-1]

def get_rechtsonder(veld, y, x):
    """ return de waarde van de cel rechtsonder de huidige cel 
   
        y: de y-positie van de huidige cel.
        x: de x-positie van de huidige cel.
        
        Als de huidige cel zich op de rechtergrens bevindt, return 0.
        Als de huidige cel zich op de ondergrens bevindt, return 0.

        veld = [
            [1, 2],
            [3, 4]
        ]

        >>> print( get_rechtsonder(veld, 1, 1) ) --> 0
        >>> print( get_rechtsonder(veld, 0, 1) ) --> 0
        >>> print( get_rechtsonder(veld, 1, 0) ) --> 0
    """
    rij = veld[y]
    if y==len(veld)-1 or x==len(rij)-1:
        return 0
    else:
        rij = veld[y+1]
        return rij[x+1]

def tel_buren(veld, y, x):
    """ return het aantal naburige cellen dat leeft

        veld: het veld met cellen.
        y: de y-positie van de huidige cel.
        x: de x-positie van de huidige cel.
    
        naburige cellen bevinden zich in de 8 posities rondom de huidige cell.
        Cellen met een waarde 1 zijn levend, cellen met een waarde 0 zijn dood.

        veld = [
            [1, 1, 0],
            [0, 1, 0],
            [1, 0, 0]
        ]

        >>> print( tel_buren(veld, 1, 0) ) --> 4
        >>> print( tel_buren(veld, 2, 1) ) --> 2
        >>> print( tel_buren(veld, 0, 0) ) --> 2
        >>> print( tel_buren(veld, 2, 0) ) --> 1
    """
    teller = 0
    if get_links(veld, y, x) == 1:
        teller = teller+1
    if get_linksboven(veld, y, x) == 1:
        teller = teller+1
    if get_boven(veld, y, x) == 1:
        teller = teller+1
    if get_rechtsboven(veld, y, x) == 1:
        teller = teller+1
    if get_rechts(veld, y, x) == 1:
        teller = teller+1
    if get_rechtsonder(veld, y, x) == 1:
        teller = teller+1
    if get_onder(veld, y, x) == 1:
        teller = teller+1
    if get_linksonder(veld, y, x) == 1:
        teller = teller+1
    return teller


def leeft_of_sterft(veld, y, x):
    """ return True als de huidige cel zal leven, False als het sterft 

        veld: het veld met cellen.
        y: de y-positie van de huidige cel.
        x: de x-positie van de huidige cel.
        
    
        De return-waarde MOET een boolean zijn. Gebruik volgende logica.
        De huidige cel is levend, het blijft leven als:
            het 2 of 3 levende buren heeft.
        De huidige cel is dood, het komt tot leven als:
            het 3 levende buren heeft.
        In alle andere gevallen wordt/blijft de huidige cel dood. 

        veld = [
            [1, 1, 0],
            [0, 1, 0],
            [1, 0, 0]
        ]

        >>> print( leeft_of_sterft(veld, 0, 0) ) --> True
        >>> print( leeft_of_sterft(veld, 0, 1) ) --> True
        >>> print( leeft_of_sterft(veld, 1, 0) ) --> False
        >>> print( leeft_of_sterft(veld, 2, 0) ) --> False
        >>> print( leeft_of_sterft(veld, 2, 1) ) --> False
        
        In dit voorbeeld blijven enkel de cel linksboven en middenboven levend (1),
        de rest gaat dood (0). Dit gebeurt in update_veld() OBV de returnde boolean.
    """
    plaats = veld[y][x]
    if plaats == 1:
        if (1 < tel_buren(veld, y, x) < 4):
            return True
        else:
            return False
    if plaats == 0:
        if tel_buren(veld, y, x) ==3:
            return True
        else:
            return False


# Je hoeft deze functie niet op te stellen. Overloop hem wel. Snap je wat er gebeurt?
# Zo nee, vraag om extra uitleg.
def update_veld(veld):
    """Update het veld volgens de regels van the game of life"""
    # Maak een kopie van het huidige veld
    huidig_veld = copy.deepcopy(veld)

    # Bepaal welke cel leeft/sterft. Update het veld op basis hiervan.s
    for y, rij in enumerate(huidig_veld):
        for x, _ in enumerate(rij):
            leeft = leeft_of_sterft(huidig_veld, y, x)
            if leeft:
                veld[y][x] = 1
            else:
                veld[y][x] = 0

# Je hoeft deze functie niet op te stellen. Overloop hem wel. Snap je wat er gebeurt?
# Zo nee, vraag om extra uitleg.
def main():
    pygame.init()
    screen = pygame.display.set_mode((BREEDTE * CEL_HOOGTE, HOOGTE * CEL_HOOGTE))
    clock = pygame.time.Clock()

    veld = maak_veld_nul(HOOGTE, BREEDTE)
    maak_veld_nul_levend(veld, KANS_LEVEND)

    running = True
    while running:
        # Maak scherm wit. Update vervolgens OBV cel-waarde.
        screen.fill((250, 250, 0))
        for y, rij in enumerate(veld):
            for x, cel in enumerate(rij):
                if cel:
                    color = (255, 0, 0)
                else:
                    color = (0, 255, 0)
                # Kleur viekant op scherm OBV kleur cel.
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(
                        x * CEL_BREEDTE,
                        y * CEL_HOOGTE,
                        CEL_BREEDTE,
                        CEL_HOOGTE,
                    ),
                )

        # Update all cellen in het veld.
        update_veld(veld)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(60)


if __name__ == "__main__":
    main()