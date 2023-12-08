import requests
class PokemonDatabaseSystem:
    def __init__(self):
        self.pokemon_db = {}
        
    # Store the data in the instance's dictionary for future use
    # Args: pokemon_name : str
    # Returns: none
    def get_data_from_api(self, pokemon_name):
        url_link = "https://pokeapi.co/api/v2/pokemon/"
        url_link += pokemon_name
        data = requests.get(url_link)
        if data.status_code == 200:
            data = data.json()
            dict_data = {
                "id": data.get("id"),
                "height": data.get("height"),
                "weight": data.get("weight")
            }
            i = 0
            while i < len(data.get("abilities")):
                name = "ability"
                name += str(i+1)
                dict_data[name] = (data.get("abilities")[i]["ability"].get("name"))
                i += 1
            self.pokemon_db[pokemon_name] = dict_data
            return self.pokemon_db
        else:
            return "Error: " + str(data.status_code)
        
    # Fetch Pokemon data either from the API or the local dictionary if available.
    # Args: pokemon_name : str
    # Returns: value of key in pokemon_db
    def get_pokemon_info(self, pokemon_name):
        if pokemon_name in self.pokemon_db:
            return self.pokemon_db[pokemon_name]
        else:
            self.get_data_from_api(pokemon_name)
            return self.pokemon_db[pokemon_name]
        
    # Show every elements of pokemon database
    # Args: none
    # Returns: pokemon_db
    def get_pokemon_db(self):
        return self.pokemon_db