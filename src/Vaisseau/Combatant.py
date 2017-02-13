from src.Arme import Blaster
from src.Arme.Arme import Arme
from src.Vaisseau.Vaisseau import Vaisseau


class Combatant(Vaisseau):
    _ID = 0
    instance = {}

    def __init__(self):
        Combatant._ID += 1

        self.armement = []

        self._mass = 100
        self.volume = 100
        self.cap_armement = 3

        self.identifiant = "HEAVY-{}".format(Combatant._ID)
        Combatant.instance[self] = self.identifiant

    def equiperArme(self, weapon):

        if weapon.location is not None:
            raise ValueError("This weapon is already on {}".format(weapon.location.identifiant))
        if not isinstance(weapon, Arme):
            raise ValueError("Only weapon can be added.")

        if weapon.actif:
            raise ValueError("Weapon {} already in use.".format(weapon.identifiant))

        if self.cap_armement == 0:
            raise ValueError("This battleship cannot bring more weapon.")

        weapon.actif = True
        self.armement.append(weapon)
        weapon.location = self
        self.cap_armement -= 1
        self.volume += weapon.volume


    def removeArme(self, weapon):
        if not isinstance(weapon, Arme):
            raise ValueError("Only weapon can be added.")

        if weapon not in self.armement:
            raise ValueError("This weapon isn't on the ship")

        self.armement.remove(weapon)
        weapon.location = None
        self.volume -= weapon.volume

    def get_mass(self):
        finalMass = self._mass
        for item in self.armement:
            finalMass += item.get_mass()

        return finalMass



    def __repr__(self):
        return "{}".format(self.identifiant)