class Rechthoek:
    def __init__(self, breedte, hoogte, x_coördinaar, y_coördinaat):
        if breedte >0:
            if hoogte >0:
                self.breedte = breedte
                self.hoogte = hoogte
        self.x_coördinaat = x_coördinaar
        self.y_coördinaat = y_coördinaat

    def omtrek(self):
        omtrek = 2*(self.breedte) + 2*(self.hoogte)
        return omtrek
    def oppervlakte(self):
        oppervlakte = self.breedte*self.hoogte
        return oppervlakte
    
    def overlapt_met(self, rechtoek):
        try:
            teller = 0
            x_coördinaten = []
            y_coördinaten = []

            x_coördinaten.append(rechtoek.x_coördinaat)
            y_coördinaten.append(rechtoek.y_coördinaat)
            x_coördinaten.append(rechtoek.x_coördinaat)
            y_coördinaten.append(rechtoek.y_coördinaat + rechtoek.hoogte)
            x_coördinaten.append(rechtoek.x_coördinaat + rechtoek.breedte)
            y_coördinaten.append(rechtoek.y_coördinaat + rechtoek.hoogte)
            x_coördinaten.append(rechtoek.x_coördinaat + rechtoek.breedte)
            y_coördinaten.append(rechtoek.y_coördinaat)

            for i in range(4):
                if (x_coördinaten[i] > self.x_coördinaat) and (x_coördinaten[i] < (self.x_coördinaat + self.breedte)):
                    if (y_coördinaten[i] > self.y_coördinaat) and (y_coördinaten[i] < (self.y_coördinaat + self.hoogte)):
                        teller = teller+1
                    else:
                        pass
                else:
                    pass
            if teller >= 1:
                return True
            else:
                return False
        except:
            return "Argument is geen Rechthoek"
    
class Punt:
    def __init__(self, x_coördinaat, y_coördinaat):
        self.x_coördinaat = x_coördinaat
        self.y_coördinaat = y_coördinaat
    
    def zit_in(self, rechthoek):
        if (self.x_coördinaat > rechthoek.x_coördinaat) and (self.x_coördinaat < (rechthoek.x_coördinaat + rechthoek.breedte)):
            x = 1
        else:
            x = 0
        if (self.y_coördinaat > rechthoek.y_coördinaat) and (self.x_coördinaat < (rechthoek.y_coördinaat + rechthoek.hoogte)):
            y = 1
        else:
            y = 0
        if (x == 1) and (y == 1):
            return True
        else:
            return False


r1 = Rechthoek(breedte=4, hoogte=5, x_coördinaar=3, y_coördinaat=3)
r2 = Rechthoek(breedte=4, hoogte=4, x_coördinaar=0, y_coördinaat=0)
r3 = Rechthoek(breedte=4, hoogte=4, x_coördinaar=100, y_coördinaat=100)
p1 = Punt(x_coördinaat=5, y_coördinaat=7)

print(r1.overlapt_met(r2)) # True
print(r1.overlapt_met(r3)) # False
print(r1.overlapt_met(p1)) # Argument is geen Rechthoek