from business_object.pokemon.abstract_pokemon import AbstractPokemon


class All_rounder_pokemon(AbstractPokemon):
    def __init__(self, stat_max=None, stat_current=None, level=0, name=None, type_pk=None):
        super.__init__(self, stat_max, stat_current, level, name, type_pk)
