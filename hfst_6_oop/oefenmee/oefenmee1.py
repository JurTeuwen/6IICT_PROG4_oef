class Hond:
    naam = "Rens"
    massa = "20kg"

    def sldkf(self):
        self.massa = "0kg"

hond = Hond()
huisdier = Hond()
hond.sldkf()

print(hond.naam, hond.massa, type(hond))
print(huisdier.naam, huisdier.massa, type(huisdier))