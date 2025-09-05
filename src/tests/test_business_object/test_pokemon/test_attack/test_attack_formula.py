from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon
from business_object.pokemon.attack.physical_formula_attack import PhysicalFormulaAttack
from business_object.statistic import Statistic


class TestAttackFormulaDamage:
    def test_attack_formula(self):
        # GIVEN
        bulldoze = PhysicalFormulaAttack(60, "bulldoze", "Lowers opponent's Speed.")
        poke1 = AllRounderPokemon(stat_current=Statistic(attack=200, defense=100))

        # WHEN
        damage = bulldoze.get_attack_stat(poke1)

        # THEN
        assert damage == 60


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
