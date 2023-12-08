from pokemon import PokemonDatabaseSystem
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

print("--- PokeAPI Manager ---")
P = PokemonDatabaseSystem()
switch = False
while switch == False:
    print("Choose option: " + "\n" + "1 - Fetch data from PokeAPI" + "\n" + "2 - Show info about pokemon" + "\n" + "3 - Show every info about pokemons in database" + "\n" + "4 - Quit")
    option = int(input("Your choice: "))
    if option == 1:
        clearConsole()
        pokemon_name = input("Enter name of pokemon: ")
        get_data = P.get_data_from_api(pokemon_name)
        if get_data == P.pokemon_db:
            print("Data was fetched correctly.")
            print("-----")
        else:
            print(get_data)
            print("-----")
    elif option == 2:
        clearConsole()
        pokemon_name = input("Enter name of pokemon: ")
        get_info = P.get_pokemon_info(pokemon_name)
        print("ID: " + str(get_info.get("id")))
        print("Height: " + str(get_info.get("height")))
        print("Weight: " + str(get_info.get("weight")))
        i = 1
        while i <= len(get_info)-3:
            index = "ability"
            index += str(i)
            print("Ability #" + str(i) + ": " + get_info.get(index))
            i += 1
        print("-----")
    elif option == 3:
        clearConsole()
        if len(P.pokemon_db) == 1:
            name = list(P.pokemon_db.keys())[0]
            print("Name: " + list(P.pokemon_db.keys())[0])
            print("ID: " + str(P.pokemon_db.get(name).get("id")))
            print("Height: " + str(P.pokemon_db.get(name).get("height")))
            print("Weight: " + str(P.pokemon_db.get(name).get("weight")))
            i = 1
            while i <= len(P.pokemon_db.get(name))-3:
                index = "ability"
                index += str(i)
                print("Ability #" + str(i) + ": " + P.pokemon_db.get(name).get(index))
                i += 1
            print("-----")
        elif len(P.pokemon_db) > 1:
            i = 0
            while i < len(P.pokemon_db):
                name = list(P.pokemon_db.keys())[i]
                print("Name: " + list(P.pokemon_db.keys())[i])
                print("ID: " + str(P.pokemon_db.get(name).get("id")))
                print("Height: " + str(P.pokemon_db.get(name).get("height")))
                print("Weight: " + str(P.pokemon_db.get(name).get("weight")))
                i += 1
                j = 1
                while j <= len(P.pokemon_db.get(name))-3:
                    index = "ability"
                    index += str(j)
                    print("Ability #" + str(j) + ": " + P.pokemon_db.get(name).get(index))
                    j += 1
                print("-----")
    elif option == 4:
        switch = True
    else:
        clearConsole()
        print("Enter correct option.")