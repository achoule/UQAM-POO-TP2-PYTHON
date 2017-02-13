from src.Arme.Phaser import Phaser
from src.Vaisseau.Combatant import Combatant


class Leger(Combatant):
    _ID = 0
    instance = {}

    def __init__(self):
        Leger._ID += 1

        self.armement = []
        self._mass = 50
        self.volume = 10
        self.cap_armement = 2
        self.identifiant = "LIGHT-{}".format(Leger._ID)
        Leger.instance[self] = self.identifiant

    def equiperArme(self, phaser):
        if not isinstance(phaser, Phaser):
            raise ValueError("This battleship can carry only Phaser.")

        Combatant.equiperArme(self, phaser)

    def __repr__(self):
        return "{}".format(self.identifiant)