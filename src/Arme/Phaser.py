from src.Arme.Arme import Arme


class Phaser(Arme):
    _ID = 0
    instance = {}
    def __init__(self):
        Phaser._ID += 1

        self._masse = 1
        self.volume = 1
        self.identifiant = "PHASER-{}".format(Phaser._ID)
        Phaser.instance[self] = self.identifiant

    def __repr__(self):
        return "{}".format(self.identifiant)
