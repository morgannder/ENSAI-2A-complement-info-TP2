from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.statistic import Statistic


class Testlevel:
    def test_level_up(self):
        # GIVEN
        tortank = AttackerPokemon(stat_current=Statistic(attack=200, defense=100))

        # WHEN
        tortank.level_up()
        level = tortank.level

        # THEN
        assert level == 1
