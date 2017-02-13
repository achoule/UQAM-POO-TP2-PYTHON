from src.Arme.Blaster import Blaster
from src.Service.StationSpatiale import StationSpatiale
from src.Vaisseau import TransportCombat
from src.Vaisseau.Combatant import Combatant

station = StationSpatiale()

print("*******Création Vaisseau Léger*******")
station.creerVaisseau("leger")
print("{}-Créé".format(station.hangarLeger))

print("*******Création Vaisseau de transport de combat*******")
station.creerVaisseau("TC")
print("{}-Créé".format(station.hangarTC))


print("*******Création Vaisseau de transport*******")
station.creerVaisseau("transport")
print("{}-Créé".format(station.hangarTransporteur))


print("*******Création de Blaster*******")

station.creerArme("blaster")
station.creerArme("blaster")
print("{}-Créé".format(station.hangarBlaster))


print("*******Création de Phaser*******")

station.creerArme("phaser")
station.creerArme("phaser")
station.creerArme("phaser")
station.creerArme("phaser")
print("{}-Créé".format(station.hangarPhaser))


print("*******Création de Conteneurs*******")

station.creerConteneur(1, 1)
station.creerConteneur(1, 1)
station.creerConteneur(1, 1)
station.creerConteneur(1, 1)
station.creerConteneur(1, 1)
station.creerConteneur(100, 10)
station.creerConteneur(100, 10)
station.creerConteneur(100, 10)
station.creerConteneur(100, 10)
print("{}-Créé".format(station.hangarConteneur))


print("*******Armement des Vaisseaux de combat Léger*******")

station.equiperArme("leger-1", "phaser-1")
station.equiperArme("leger-1", "phaser-2")
print("{}-Equipé".format(station.rechercherElement("leger-1").armement))

print("*******Chargement des conteneurs dans le vaisseau de transport*******")

station.chargerFret("transport-1", "conteneur-1")
station.chargerFret("transport-1", "conteneur-2")
station.chargerFret("transport-1", "conteneur-3")
station.chargerFret("transport-1", "conteneur-4")
station.chargerFret("transport-1", "conteneur-5")
print("{}-Equipé".format(station.rechercherElement("transport-1").stuff))


print("*******Chargement d'un vaisseau léger dans le vaisseau de transport*******")

station.chargerFret("transport-1", "leger-1")
print("{}-Equipé".format(station.rechercherElement("transport-1").stuff))


print("*******Désarmement d'un Phaser du vaisseau de combat léger*******")

station.retirerArme("leger-1", "phaser-1")
print("{}-removed".format(station.rechercherElement("leger-1").armement))


print("*******Chargement d'un Phaser dans le vaisseau de transport*******")

station.chargerFret("transport-1", "phaser-1")
print("{}-Equipé".format(station.rechercherElement("transport-1").stuff))

print("*******Armement du vaisseau de transport de combat*******")

station.equiperArme("tc-1", "blaster-1")
station.equiperArme("tc-1", "blaster-2")
station.equiperArme("tc-1", "phaser-3")
station.equiperArme("tc-1", "phaser-4")
print("{}-Equipé".format(station.rechercherElement("tc-1").armement))


print("*******Chargement du vaisseau de transport dans le vaisseau de transport de combat*******")

station.chargerFret("tc-1", "transport-1")
print("{}-Equipé".format(station.rechercherElement("tc-1").stuff))


print("*******Chargement de conteneurs dans le vaisseau de transprot de combat*******")

station.chargerFret("tc-1", "conteneur-6")
station.chargerFret("tc-1", "conteneur-7")
station.chargerFret("tc-1", "conteneur-8")
station.chargerFret("tc-1", "conteneur-9")
print("{}-Equipé".format(station.rechercherElement("tc-1").stuff))

print("*******Recharge en gaz des blasters*******")

for item in station.hangarBlaster:
    item.recharger()
print("{}-Recharger".format(station.hangarBlaster))

print("*******Information sur le Transport de combat  : *******")

print("Masse total : {} t".format(station.rechercherElement("tc-1").get_mass()))
print("Capacitée Volumique restante : {} m^3".format(station.rechercherElement("tc-1").cap_volumique))




