from abstract_pokemon import AbstractPokemon


class AttackerPokemon(AbstractPokemon):
    """ """

    def __init__(self, stat_max=None, stat_current=None, level=0, name=None):
        super().__init__(stat_max, stat_current, level, name, "Attacker")

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.speed_current + self.attack_current) / 200
