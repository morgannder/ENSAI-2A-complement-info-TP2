from business_object.pokemon.attack.abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    def __init__(self, power=0, name=None, desc=None):
        super().__init__(power, name, desc)

    def compute_damage(self, APkm1, APkm2):
        return self.power
