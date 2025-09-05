from abc import abstractmethod

from business_object.pokemon.attack.abstract_attack import AbstractAttack


class AbstractFormulaAttack(AbstractAttack):
    def __init__(self, power=0, name=None, desc=None, attacktype=None):
        super().__init__(power, name, desc, attacktype)

    def compute_damage(self, APkm1, APkm2):
        return self.power

    @abstractmethod
    def get_attack_stat(self, Akpm):
        pass

    @abstractmethod
    def get_defense_stat(self, Akpm, type):
        pass
