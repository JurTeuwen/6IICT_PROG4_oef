class Rechthoek:
    def __init__(self, breedte, hoogte):
        if breedte >0:
            if hoogte >0:
                self.breedte = breedte
                self.hoogte = hoogte

    def omtrek(self):
        omtrek = 2*(self.breedte) + 2*(self.hoogte)
        return omtrek
    def oppervlakte(self):
        oppervlakte = self.breedte*self.hoogte
        return oppervlakte
    def vergelijk_omtrek(self, getal):
        omtrek = 2*(self.breedte) + 2*(self.hoogte)
        if omtrek > getal:
            print("Getal is kleiner dan omtrek rechthoek.")
        elif omtrek == getal:
            print("Getal is gelijk aan omtrek rechthoek.")
        else:
            print("Getal is groter dan omtrek rechthoek.")
    def vergelijk_oppervlakte(self, getal):
        oppervlakte = self.breedte*self.hoogte
        if oppervlakte > getal:
            print("Getal is kleiner dan opp rechthoek.")
        elif oppervlakte == getal:
            print("Getal is gelijk aan opp rechthoek.")
        else:
            print("Getal is groter dan opp rechthoek.")
    
r1 = Rechthoek(breedte=4, hoogte=5)
r1.vergelijk_omtrek(15)         # Getal is kleiner dan omtrek rechthoek.
r1.vergelijk_oppervlakte(20)    # Getal is gelijk aan opp rechthoek.