import unittest
from unittest import mock, TestCase
from pokemon import PokemonDatabaseSystem

class TestGetData(unittest.TestCase):
    def mocked_return_get_data(*args, **kwargs):
        return {'bulbasaur': {'id': 1, 'height': 7, 'weight': 69, 'ability1': 'overgrow', 'ability2': 'chlorophyll'}}
    
    @mock.patch("pokemon.PokemonDatabaseSystem.get_data_from_api", new=mocked_return_get_data)
    def test_get_data_mocked(self):
        pokemon = PokemonDatabaseSystem()
        get_data = pokemon.get_data_from_api("name")
        self.assertEqual(get_data, {'bulbasaur': {'id': 1, 'height': 7, 'weight': 69, 'ability1': 'overgrow', 'ability2': 'chlorophyll'}})
    
    def mocked_return_get_data_wrong_name(*args, **kwargs):
        return "Error: 404"
    
    @mock.patch("pokemon.PokemonDatabaseSystem.get_data_from_api", new=mocked_return_get_data_wrong_name)
    def test_get_data_wrong_name_mocked(self):
        pokemon = PokemonDatabaseSystem()
        get_data = pokemon.get_data_from_api("wrong_name")
        self.assertEqual(get_data, "Error: 404")
        
class TestGetInfo(unittest.TestCase):
    def mocked_return_get_info_exist(*args, **kwargs):
        return {'id': 25, 'height': 4, 'weight': 60, 'ability1': 'static', 'ability2': 'lightning-rod'}
    
    @mock.patch("pokemon.PokemonDatabaseSystem.get_pokemon_info", new=mocked_return_get_info_exist)
    def test_get_info_exist_mocked(self):
        pokemon = PokemonDatabaseSystem()
        pokemon.pokemon_db["pikachu"] = {'id': 25, 'height': 4, 'weight': 60, 'ability1': 'static', 'ability2': 'lightning-rod'}
        get_info_exist = pokemon.get_pokemon_info("pikachu")
        self.assertEqual(get_info_exist, {'id': 25, 'height': 4, 'weight': 60, 'ability1': 'static', 'ability2': 'lightning-rod'})

    def mocked_return_info_new(*args, **kwargs):
        return {'id': 25, 'height': 4, 'weight': 60, 'ability1': 'static', 'ability2': 'lightning-rod'}
    
    @mock.patch("pokemon.PokemonDatabaseSystem.get_pokemon_info", new=mocked_return_info_new)
    def test_get_info_new_mocked(self):
        pokemon = PokemonDatabaseSystem()
        get_info_new = pokemon.get_pokemon_info("pikachu")
        self.assertEqual(get_info_new, {'id': 25, 'height': 4, 'weight': 60, 'ability1': 'static', 'ability2': 'lightning-rod'})
        
        
if __name__ == '__main__':
    unittest.main()