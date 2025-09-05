from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon
from business_object.pokemon.attack.fixed_damage_attack import FixedDamageAttack
from business_object.statistic import Statistic


class TestAttackDamage:
    def test_compute_damage(self):
        # GIVEN
        bulldoze = FixedDamageAttack(60, "bulldoze", "Lowers opponent's Speed.")
        poke1 = AllRounderPokemon(stat_current=Statistic(attack=200, defense=100))
        poke2 = AllRounderPokemon(stat_current=Statistic(attack=200, defense=100))

        # WHEN
        damage = bulldoze.compute_damage(poke1, poke2)

        # THEN
        assert damage == 60


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
