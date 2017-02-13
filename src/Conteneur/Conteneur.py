from src.ElementPhysique import ElementPhysique


class Conteneur(ElementPhysique):
    _ID = 0
    instance = {}
    def __init__(self, masse, volume):
        Conteneur._ID += 1

        ElementPhysique.__init__(self)

        self._mass = masse
        self.volume = volume

        self.identifiant = "CONTENDER-{}".format(Conteneur._ID)
        Conteneur.instance[self] = self.identifiant

    def __repr__(self):
        return "{}, {}x{}".format(self.identifiant, self._mass, self.volume)