class Hond:
    def benoem(self, naam):
        self.naam = naam
    def wegen(self, massa):
        self.massa = massa
    def blaf(self):
        print(f"{self.naam} zegt blaf")
    def weegschaal(self):
        print(f"{self.naam} weegt {self.massa}kg")

hond = Hond()
hond.benoem("Fleur")
hond.blaf()

dier = Hond()
dier.benoem("Fifi")
dier.wegen(3)
dier.weegschaal()

hond.weegschaal()
