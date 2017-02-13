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
    
    # stoque des différents objets 
    hangarLourd = []
    hangarLeger = []
    hangarTC = []
    hangarTransporteur = []

    hangarBlaster = []
    hangarPhaser = []

    hangarConteneur = []

    #Type attendu : lourd / leger / tc ou transport
    def creerVaisseau(self, type):

        typeUp = type.upper() #gestion de la casse

        if typeUp == "LOURD":
            vaisseau = Combatant()
            self.hangarLourd.append(vaisseau)
        elif typeUp == "LEGER":
            vaisseau = Leger()
            self.hangarLeger.append(vaisseau)
        elif typeUp == "TC":
            vaisseau = TransportCombat()
            self.hangarTC.append(vaisseau)
        elif typeUp == "TRANSPORT":
            vaisseau = Transport()
            self.hangarTransporteur.append(vaisseau)
        else:
            raise ValueError("Le type doit-être : Lourd / Leger / TC ou Transport.")

    #type attendu : blaster ou phaser
    def creerArme(self, type):

        typeUp = type.upper()
        if typeUp == "PHASER":
            arme = Phaser()
            self.hangarPhaser.append(arme)
        elif typeUp == "BLASTER":
            arme = Blaster()
            self.hangarBlaster.append(arme)

    def creerConteneur(self, masse, volume):
        conteneur = Conteneur(masse, volume)
        self.hangarConteneur.append(conteneur)

    #referencer l'identifiant du vaisseau à équiper puis de l'arme à mettre dessus
    def equiperArme(self, id, id_arme):
        vaisseau = self.rechercherElement(id)
        arme = self.rechercherElement(id_arme)

        if not isinstance(vaisseau, Combatant):
            raise ValueError("Le vaisseau doit-être un vaisseau de combat !")

        if not isinstance(arme, Arme):
            raise ValueError("L'arme doit être une arme valide !")

        if isinstance(arme, Blaster) and len(self.hangarBlaster) > 0:
            vaisseau.equiperArme(arme)
            self.hangarBlaster.remove(arme)
        elif isinstance(arme, Phaser) and len(self.hangarPhaser) > 0:
            vaisseau.equiperArme(arme)
            self.hangarPhaser.remove(arme)
        else:
            raise ValueError("arme must be blaster or phaser and available in stock")


    def retirerArme(self, id, id_arme):
        vaisseau = self.rechercherElement(id)
        arme = self.rechercherElement(id_arme)

        vaisseau.retirerArme(arme)

        if isinstance(arme, Blaster):
            self.hangarBlaster.append(arme)
        elif isinstance(arme, Phaser):
            self.hangarPhaser.append(arme)

    def chargerFret(self, id, id_stuff):
        vaisseau = self.rechercherElement(id)
        fret = self.rechercherElement(id_stuff)

        if not isinstance(vaisseau, Transport):
            raise ValueError("Le vaisseau doit être un transporteur!")


        vaisseau.chargerFret(fret)

    def retirerFret(self, id, id_stuff):
        vaisseau = self.rechercherElement(id)
        fret = self.rechercherElement(id_stuff)

        if not isinstance(vaisseau, Transport):
            raise ValueError("Le vaisseau doit être un transporteur !")

        vaisseau.retirerFret(fret)

    def recharger(self, id):
        arme = self.rechercherElement(id)
        if not isinstance(arme, Blaster):
            raise ValueError("L'arme doit être un Blaster ! ")
        arme.recharger()

    def localiserElement(self, id):
        element = self.rechercherElement(id)

        if element.location == None:
            location = "Dans le Hangar."
        else:
            location = element.location
        return location

    def rechercherElement(self, id=""):
        idUpper = id.upper()
        splited = idUpper.split('-', 1)[0]

        if splited == "LOURD":
            objectType = Combatant
        elif splited == "LEGER":
            objectType = Leger
        elif splited == "TC":
            objectType = TransportCombat
        elif splited == "TRANSPORT":
            objectType = Transport
        elif splited == "PHASER":
            objectType = Phaser
        elif splited == "BLASTER":
            objectType = Blaster
        elif splited == "CONTENEUR":
            objectType = Conteneur
        else:
            raise ValueError("L'id doit contenir : Lourd / Leger / TC / Transport / Phaser / Blaser ou Conteneur.")

        for item in objectType.instance:
            if item.identifiant == idUpper:
                return item

        raise ValueError("Element non trouvé.")