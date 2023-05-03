class Auto:
    def __init__(self, verbruik, kleur, tank_vol, tank_huidig):
        self.verbruik = verbruik
        self.kleur = kleur
        self.tank_vol = tank_vol
        self.tank_huidig = tank_huidig
    def verven(self, nieuwe_kleur):
        self.kleur = nieuwe_kleur
        print(f"Mijn auto is nu {self.kleur}.")
    def check_tank(self):
        x = self.verbruik*self.tank_huidig
        print(f"Met een tank van {self.tank_huidig} liter, kan ik nog {x} km rijden.")
    def tanken(self):
        self.tank_huidig = self.tank_vol
    def rijden(self, afstand):
        if afstand <= self.verbruik*self.tank_huidig:
            self.tank_huidig -= afstand/self.verbruik
            print(f"{afstand} km afgelegd, nog {self.tank_huidig} liter over.")
        else:
            print(f"Kan niet zover rijden op een tank van {self.tank_huidig} liter.")


auto = Auto(verbruik=20, kleur="rood", tank_vol=100, tank_huidig=30)
auto.verven("blauw") # Mijn auto is nu blauw.

auto.check_tank()    # Met een tank van 30 liter, kan ik nog 600km rijden.
auto.rijden(400)     # 400km afgelegd, nog 10.0 liter over.
auto.check_tank()    # Met een tank van 10 liter, kan ik nog 200km rijden.

auto.rijden(400)     # Kan niet zover rijden op een tank van 10.0 liter.
auto.tanken()
auto.check_tank()    # Met een tank van 100 liter, kan ik nog 2000km rijden.