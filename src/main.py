from src.Arme.Blaster import Blaster
from src.Service.StationSpatiale import StationSpatiale
from src.Vaisseau import TransportCombat
from src.Vaisseau.Combatant import Combatant

# Le Main fait office de scénario de requête style API
# Démarrage du scénario
station = StationSpatiale()

# Étape 1 - Création vaisseau de combat léger VC-1
print("\nÉtape 1 - Création vaisseau de combat léger VC-1")
station.creerVaisseau("leger")
print("{}-Créé".format(station.hangarLeger))


# Étape 2 - Équipement de deux phasers à VC-1
print("\nÉtape 2 - Équipement de deux phasers à VC-1")
station.creerArme("phaser")
station.creerArme("phaser")

station.equiperArme("leger-1", "phaser-1")
station.equiperArme("leger-1", "phaser-2")
print("{}-Equipé".format(station.rechercherElement("leger-1").armement))


# Étape 3 - Création de vaisseau de transport VT-2
print("\nÉtape 3 - Création de vaisseau de transport VT-2")
station.creerVaisseau("transport")
print("{}-Créé".format(station.hangarTransporteur))


# Étape 4 - Chargement de 5 conteneurs à VT-2
print("\nÉtape 4 - Chargement de 5 conteneurs à VT-2")
station.creerConteneur(1, 1)
station.creerConteneur(1, 1)
station.creerConteneur(1, 1)
station.creerConteneur(1, 1)
station.creerConteneur(1, 1)

station.chargerFret("transport-1", "conteneur-1")
station.chargerFret("transport-1", "conteneur-2")
station.chargerFret("transport-1", "conteneur-3")
station.chargerFret("transport-1", "conteneur-4")
station.chargerFret("transport-1", "conteneur-5")
print("{}-Equipé".format(station.rechercherElement("transport-1").stuff))


# Étape 5 - Chargement de VC-1 dans VT-2
print("\nÉtape 5 - Chargement de VC-1 dans VT-2")
station.chargerFret("transport-1", "leger-1")
print("{}-Equipé".format(station.rechercherElement("transport-1").stuff))


# Étape 6 - Déséquiper un phaser de VC-1 et le charger sur VT-2
print("\nÉtape 6 - Déséquiper un phaser de VC-1 et le charger sur VT-2")
station.retirerArme("leger-1", "phaser-1")
print("{}-removed".format(station.rechercherElement("leger-1").armement))

station.chargerFret("transport-1", "phaser-1")
print("{}-Equipé".format(station.rechercherElement("transport-1").stuff))


# Étape 7 - Création du transport de combat MR-63
print("\nÉtape 7 - Création du transport de combat MR-63")
station.creerVaisseau("TC")
print("{}-Créé".format(station.hangarTC))


# Étape 8 - Équipement de deux phasers et deux blasters à MR-63
print("\nÉtape 8 - Équipement de deux phasers et deux blasters à MR-63")
station.creerArme("phaser")
station.creerArme("phaser")
print("{}-Créé".format(station.hangarPhaser))

station.creerArme("blaster")
station.creerArme("blaster")
print("{}-Créé".format(station.hangarBlaster))

station.equiperArme("tc-1", "blaster-1")
station.equiperArme("tc-1", "blaster-2")
station.equiperArme("tc-1", "phaser-3")
station.equiperArme("tc-1", "phaser-4")
print("{}-Equipé".format(station.rechercherElement("tc-1").armement))


# Étape 8 - Chargement de 4 conteneurs et de VT-2
print("\nÉtape 8 - Chargement de 4 conteneurs et de VT-2")
station.creerConteneur(100, 10)
station.creerConteneur(100, 10)
station.creerConteneur(100, 10)
station.creerConteneur(100, 10)
print("{}-Créé".format(station.hangarConteneur))

station.chargerFret("tc-1", "conteneur-6")
station.chargerFret("tc-1", "conteneur-7")
station.chargerFret("tc-1", "conteneur-8")
station.chargerFret("tc-1", "conteneur-9")
print("{}-Equipé".format(station.rechercherElement("tc-1").stuff))

station.chargerFret("tc-1", "transport-1")
print("{}-Equipé".format(station.rechercherElement("tc-1").stuff))


# Étape 9 - Affichage de la masse totale et du volume disponible de MR-63
print("\nÉtape 9 - Affichage de la masse totale et du volume disponible de MR-63")
print("Masse total : {} t".format(station.rechercherElement("tc-1").get_mass()))
print("Capacitée Volumique restante : {} m^3".format(station.rechercherElement("tc-1").cap_volumique))


# Étape 10 - Affichage des positions de chaque phaser
print("\nÉtape 10 - Affichage des positions de chaque phaser")
print("{}-Equipé".format(station.localiserElement("phaser-1")))
print("{}-Equipé".format(station.localiserElement("phaser-2")))
print("{}-Equipé".format(station.localiserElement("phaser-3")))
print("{}-Equipé".format(station.localiserElement("phaser-4")))


# Étape 11 - Affichage du niveau de gaz et rechargement des blasters de MR-63
print("\nÉtape 11 - Affichage du niveau de gaz et rechargement des blasters de MR-63")
for item in station.hangarBlaster:
    item.recharger()
print("{}-Recharger".format(station.hangarBlaster))




