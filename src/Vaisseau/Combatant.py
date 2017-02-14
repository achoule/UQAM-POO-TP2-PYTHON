from src.Arme.Arme import Arme
from src.Vaisseau.Vaisseau import Vaisseau


class Combatant(Vaisseau):
    _ID = 0
    instance = {}

    def __init__(self):
        Combatant._ID += 1

        self.armement = []

        self._masse = 100
        self.volume = 100
        self.cap_armement = 3

        self.identifiant = "LOURD-{}".format(Combatant._ID)
        Combatant.instance[self] = self.identifiant

    def equiperArme(self, arme):

        if arme.location is not None:
            raise ValueError("Cette arme est déjà dans : {}".format(arme.location.identifiant))
        if not isinstance(arme, Arme):
            raise ValueError("Seule une arme peut être équipé.")

        if arme.actif:
            raise ValueError("L'arme {} est déjà utilisée.".format(arme.identifiant))

        if self.cap_armement == 0:
            raise ValueError("Ce vaisseau ne peut contenir plus d'arme.")

        arme.actif = True
        self.armement.append(arme)
        arme.location = self
        self.cap_armement -= 1
        self.volume += arme.volume

    def retirerArme(self, arme):
        if not isinstance(arme, Arme):
            raise ValueError("Seule une arme peut être équipée.")

        if arme not in self.armement:
            raise ValueError("Cette arme n'est pas sur le vaisseau.")

        self.armement.remove(arme)
        arme.location = None
        self.volume -= arme.volume

    def get_mass(self):
        finalMasse = self._masse
        for item in self.armement:
            finalMasse += item.get_mass()

        return finalMasse

    def __repr__(self):
        return "{}".format(self.identifiant)
