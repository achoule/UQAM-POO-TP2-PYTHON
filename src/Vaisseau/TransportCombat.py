from src.Vaisseau.Combatant import Combatant
from src.Vaisseau.Transport import Transport


class TransportCombat(Combatant, Transport):
    _ID = 0
    instance = {}

    def __init__(self):
        TransportCombat._ID += 1

        self.armement = []
        self.stuff = []

        self._mass = 150
        self.volume = 200
        self.cap_armement = 5
        self.cap_volumique = 180
        self.cap_massique = 600

        self.identifiant = "TC-{}".format(TransportCombat._ID)
        self.instance[self] = self.identifiant

    def __repr__(self):
        return "{}".format(self.identifiant)

    def get_mass(self):
        return Combatant.get_mass(self) + Transport.get_mass(self) - self._mass