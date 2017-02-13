from src.Conteneur.Conteneur import Conteneur
from src.ElementPhysique import ElementPhysique
from src.Arme.Arme import Arme
from src.Arme.Blaster import Blaster
from src.Arme.Phaser import Phaser

from src.Singleton import Singleton

from src.Vaisseau.Combatant import Combatant
from src.Vaisseau.Leger import Leger
from src.Vaisseau.Transport import Transport
from src.Vaisseau.TransportCombat import TransportCombat


class StationSpatiale(metaclass=Singleton):
    heavyStock = []
    lightStock = []
    TCStock = []
    transporterStock = []

    blasterStock = []
    phaserStock = []

    contenderStock = []

    def createShip(self, type):

        typeUp = type.upper()

        if typeUp == "HEAVY":
            ship = Combatant()
            self.heavyStock.append(ship)
        elif typeUp == "LIGHT":
            ship = Leger()
            self.lightStock.append(ship)
        elif typeUp == "TC":
            ship = TransportCombat()
            self.TCStock.append(ship)
        elif typeUp == "TRANSPORT":
            ship = Transport()
            self.transporterStock.append(ship)
        else:
            raise ValueError("type must be : heavy / light / TC or transport.")

    def createWeapon(self, type):

        typeUp = type.upper()
        if typeUp == "PHASER":
            weapon = Phaser()
            self.phaserStock.append(weapon)
        elif typeUp == "BLASTER":
            weapon = Blaster()
            self.blasterStock.append(weapon)

    def createContener(self, masse, volume):
        contender = Conteneur(masse, volume)
        self.contenderStock.append(contender)

    def equipWeapon(self, id, id_weapon):
        ship = self.findElement(id)
        weapon = self.findElement(id_weapon)

        if not isinstance(ship, Combatant):
            raise ValueError("Ship must be a battleShip !")

        if not isinstance(weapon, Arme):
            raise ValueError("Weapon must be a Weapon !")

        if isinstance(weapon, Blaster) and len(self.blasterStock) > 0:
            ship.equiperArme(weapon)
            self.blasterStock.remove(weapon)
        elif isinstance(weapon, Phaser) and len(self.phaserStock) > 0:
            ship.equiperArme(weapon)
            self.phaserStock.remove(weapon)
        else:
            raise ValueError("Weapon must be blaster or phaser and available in stock")


    def takeOffWeapon(self, id, id_weapon):
        ship = self.findElement(id)
        weapon = self.findElement(id_weapon)

        ship.removeArme(weapon)

        if isinstance(weapon, Blaster):
            self.blasterStock.append(weapon)
        elif isinstance(weapon, Phaser):
            self.phaserStock.append(weapon)

    def chargeStuff(self, id, id_stuff):
        ship = self.findElement(id)
        stuff = self.findElement(id_stuff)

        if not isinstance(ship, Transport):
            raise ValueError("Ship must be a transporter !")


        ship.chargeStuff(stuff)

    def removeStuff(self, id, id_stuff):
        ship = self.findElement(id)
        stuff = self.findElement(id_stuff)

        if not isinstance(ship, Transport):
            raise ValueError("Ship must be a transporter !")

        ship.removeStuff(stuff)

    def reload(self, id):
        weapon = self.findElement(id)
        if not isinstance(weapon, Blaster):
            raise ValueError("Weapon must be a blaster ! ")
        weapon.reload()

    def itemLocalisation(self, id):
        item = self.findElement(id)

        if item.location == None:
            location = "On the stockage"
        else:
            location = item.location
        return location

    def findElement(self, id=""):
        idUpper = id.upper()
        splited = idUpper.split('-', 1)[0]

        if splited == "HEAVY":
            objectType = Combatant
        elif splited == "LIGHT":
            objectType = Leger
        elif splited == "TC":
            objectType = TransportCombat
        elif splited == "TRANSPORT":
            objectType = Transport
        elif splited == "PHASER":
            objectType = Phaser
        elif splited == "BLASTER":
            objectType = Blaster
        elif splited == "CONTENDER":
            objectType = Conteneur
        else:
            raise ValueError("Id must contain : Heavy , Light , TC ,Contender , Blaster or Phaser.")

        for item in objectType.instance:
            if item.identifiant == idUpper:
                return item

        raise ValueError("Ship or weapon not found")