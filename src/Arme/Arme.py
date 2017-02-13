from abc import ABCMeta

from src.ElementPhysique import ElementPhysique


class Arme(ElementPhysique, metaclass=ABCMeta):
    actif = False