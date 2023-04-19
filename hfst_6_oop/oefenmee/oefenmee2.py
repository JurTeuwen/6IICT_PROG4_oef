class Hond:
    naam = "Rens"
    massa = "20"
    def blaf(self):
        print(f"{self.naam} zegt blaf")
    def weegschaal(zichzelf):
        print(f"{zichzelf.naam} weegt {zichzelf.massa}kg")

hond = Hond()
huisdier = Hond()

print(hond.naam, hond.massa, type(hond))
hond.blaf()
hond.weegschaal()
print(huisdier.naam, huisdier.massa, type(huisdier))
huisdier.blaf()
huisdier.weegschaal()