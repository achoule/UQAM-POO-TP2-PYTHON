from src.Arme.Arme import Arme


class Blaster(Arme):
    _ID = 0
    instance = {}

    def __init__(self):
        Blaster._ID += 1

        self.pourcentage_gaz = 0
        self._masse = 2
        self.volume = 2
        self.identifiant = "BLASTER-{}".format(Blaster._ID)
        Blaster.instance[self] = self.identifiant

    def recharger(self):
        self.pourcentage_gaz = 100

    def __repr__(self):
        return "{} - gaz : {}%".format(self.identifiant, self.pourcentage_gaz)
