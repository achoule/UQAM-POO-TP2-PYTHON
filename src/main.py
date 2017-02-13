from src.Arme.Blaster import Blaster
from src.Service.StationSpatiale import StationSpatiale
from src.Vaisseau import TransportCombat
from src.Vaisseau.Combatant import Combatant

station = StationSpatiale()

print("*******Light BattleShip Creation*******")
station.createShip("light")
print("{}-Created".format(station.lightStock))

print("*******Transport-BattleShip Creation*******")
station.createShip("TC")
print("{}-Created".format(station.TCStock))


print("*******Light BattleShip Creation*******")
station.createShip("transport")
print("{}-Created".format(station.transporterStock))


print("*******Blaster Creation*******")

station.createWeapon("blaster")
station.createWeapon("blaster")
print("{}-Created".format(station.blasterStock))


print("*******Phaser Creation*******")

station.createWeapon("phaser")
station.createWeapon("phaser")
station.createWeapon("phaser")
station.createWeapon("phaser")
print("{}-Created".format(station.phaserStock))


print("*******Contender Creation*******")

station.createContener(1, 1)
station.createContener(1, 1)
station.createContener(1, 1)
station.createContener(1, 1)
station.createContener(1, 1)
station.createContener(100, 10)
station.createContener(100, 10)
station.createContener(100, 10)
station.createContener(100, 10)
print("{}-Created".format(station.contenderStock))


print("*******Phaser on Light BattleShip*******")

station.equipWeapon("light-1", "phaser-1")
station.equipWeapon("light-1", "phaser-2")
print("{}-Equipped".format(station.findElement("light-1").armement))

print("*******Contender on Transporter*******")

station.chargeStuff("transport-1", "contender-1")
station.chargeStuff("transport-1", "contender-2")
station.chargeStuff("transport-1", "contender-3")
station.chargeStuff("transport-1", "contender-4")
station.chargeStuff("transport-1", "contender-5")
print("{}-Equipped".format(station.findElement("transport-1").stuff))


print("*******Light BattleShip on Transporter*******")

station.chargeStuff("transport-1", "light-1")
print("{}-Equipped".format(station.findElement("transport-1").stuff))


print("*******Phaser out of Light BattleShip*******")

station.takeOffWeapon("light-1", "phaser-1")
print("{}-removed".format(station.findElement("light-1").armement))


print("*******Phaser on transporter*******")

station.chargeStuff("transport-1", "phaser-1")
print("{}-Equipped".format(station.findElement("transport-1").stuff))

print("*******Weapon on Transport-BattleShip*******")

station.equipWeapon("tc-1", "blaster-1")
station.equipWeapon("tc-1", "blaster-2")
station.equipWeapon("tc-1", "phaser-3")
station.equipWeapon("tc-1", "phaser-4")
print("{}-Equipped".format(station.findElement("tc-1").armement))


print("*******Transporter on Transport-BattleShip*******")

station.chargeStuff("tc-1", "transport-1")
print("{}-Equipped".format(station.findElement("tc-1").stuff))


print("*******Contender on Transport-BattleShip*******")

station.chargeStuff("tc-1", "contender-6")
station.chargeStuff("tc-1", "contender-7")
station.chargeStuff("tc-1", "contender-8")
station.chargeStuff("tc-1", "contender-9")
print("{}-Equipped".format(station.findElement("tc-1").stuff))

print("*******Blasters Reload*******")

for item in station.blasterStock:
    item.reload()
print("{}-Reloaded".format(station.blasterStock))

print("*******Transpor-BattleShip information : *******")

print("Total Mass : {} t".format(station.findElement("tc-1").get_mass()))
print("Capacity Volumique still available : {} m^3".format(station.findElement("tc-1").cap_volumique))




