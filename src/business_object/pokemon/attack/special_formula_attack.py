from business_object.pokemon.attack.abstract_formula_attack import AbstractFormulaAttack


class SpecialFormulaAttack(AbstractFormulaAttack):
    def __init__(self, power=0, name=None, desc=None):
        super().__init__(power, name, desc, "Special")

    def get_attack_stat(self, Akpm):
        return Akpm.sp_atk

    def get_defense_stat(self, Akpm):
        return Akpm.sp_def
