class Familie:
    ras = "mens"
    def __init__(self, geslacht, haar, leeftijd, naam):
        self.geslacht = geslacht
        self.haar = haar
        self.leeftijd = leeftijd
        self.naam = naam
    def is_leeftijd(self):
        return self.leeftijd
    def is_geslacht(self):
        return self.geslacht
    def verjaardag(self):
        self.leeftijd += 1
        print(f"Gefeliciteerd {self.naam}, je bent nu {self.leeftijd}.")
    def verf_haar(self, haarkleur):
        self.haar = haarkleur
        print(f"{self.naam} is nu {self.haar}.")
    def uitleg(self):
        print(f"{self.naam}: {self.geslacht}, {self.leeftijd}, {self.haar}, {self.ras}.")


vader = Familie(geslacht="man", haar="zwart", leeftijd=39, naam="Steve")

print(vader.is_leeftijd())  # 39
print(vader.is_geslacht())  # man
vader.verjaardag()          # Gefeliciteerd Steve, je bent nu 40
vader.verf_haar("blond")    # Steve is nu blond
vader.uitleg()              # Steve: man, 40, blond, mens