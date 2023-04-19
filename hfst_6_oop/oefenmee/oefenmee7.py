class Hond:
    def __init__(self, naam, massa):
        self.naam = naam
        self.massa = massa
    def wijzig_naam(self, naam):
        print(f"{self.naam} heet nu {naam}.")
        self.naam = naam
    def blaf(self):
        print(f"{self.naam} zegt blaf.")
    def weegschaal(self):
        print(f"{self.naam} weegt {self.massa}kg.")
    def eten(self, hoeveelheid):
        print(f"{self.naam} weegt nu {self.massa+(hoeveelheid*0.3)}kg.")
        self.massa=self.massa+(hoeveelheid*0.3)

hond = Hond("Lucky", 5)
hond_2 = Hond("Fleur", 8)

hond.wijzig_naam("Bolly")
hond.eten(0.5)
hond.eten(0.5)
hond.eten(0.5)
hond_2.eten(0.5)
hond_2.eten(0.5)
hond_2.eten(0.5)