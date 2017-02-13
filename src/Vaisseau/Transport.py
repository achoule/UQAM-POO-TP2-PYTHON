from src.ElementPhysique import ElementPhysique
from src.Vaisseau.Vaisseau import Vaisseau


class Transport(Vaisseau):
    _ID = 0
    instance = {}

    def __init__(self):
        Transport._ID += 1

        self.stuff = []

        self._mass = 100
        self.volume = 100
        self.cap_volumique = 90
        self.cap_massique = 300

        self.identifiant = "TRANSPORT-{}".format(Transport._ID)
        Transport.instance[self] = self.identifiant

    def chargeStuff(self, item):

        if item.location is not None:
            raise ValueError("This item is already on {}".format(item.location.identifiant))
        if not isinstance(item, ElementPhysique):
            raise ValueError("You cannot add this item on this ship")

        if self.cap_massique - item.get_mass() < 0:
            raise ValueError("You don't have enough place to stock this")

        if self.cap_volumique - item.volume < 0:
            raise ValueError("You don't have enough place to stock this")

        self.stuff += [item]
        item.location = self

        self.cap_massique -= item.get_mass()
        self.cap_volumique -= item.volume

    def removeStuff(self, item):
        if not item in self.stuff:
            raise ValueError("This item is not on the ship")

        self.stuff.remove(item)
        item.location = None

        self.cap_volumique += item.volume

    def get_mass(self):
        finalMass = self._mass
        for item in self.stuff:
            finalMass += item.get_mass()

        return finalMass

    def __repr__(self):
        return "{}".format(self.identifiant)
