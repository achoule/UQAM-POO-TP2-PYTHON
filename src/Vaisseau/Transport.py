from src.ElementPhysique import ElementPhysique
from src.Vaisseau.Vaisseau import Vaisseau


class Transport(Vaisseau):
    _ID = 0
    instance = {}

    def __init__(self):
        Transport._ID += 1

        self.stuff = []

        self._masse = 100
        self.volume = 100
        self.cap_volumique = 90
        self.cap_massique = 300

        self.identifiant = "TRANSPORT-{}".format(Transport._ID)
        Transport.instance[self] = self.identifiant

    def chargerFret(self, item):

        if item.location is not None:
            raise ValueError("Cet objet est déjà sur : {}".format(item.location.identifiant))
        if not isinstance(item, ElementPhysique):
            raise ValueError("Vous ne pouvez pas charger cet objet sur le vaisseau.")

        if self.cap_massique - item.get_mass() < 0:
            raise ValueError("Cet objet est trop lourd.")

        if self.cap_volumique - item.volume < 0:
            raise ValueError("Cet objet est trop gros.")

        self.stuff += [item]
        item.location = self

        self.cap_massique -= item.get_mass()
        self.cap_volumique -= item.volume

    def retirerFret(self, item):
        if not item in self.stuff:
            raise ValueError("Cet objet n'est pas sur le vaisseau.")

        self.stuff.remove(item)
        item.location = None

        self.cap_volumique += item.volume

    def get_mass(self):
        finalMasse = self._masse
        for item in self.stuff:
            finalMasse += item.get_mass()

        return finalMasse

    def __repr__(self):
        return "{}".format(self.identifiant)
