def evolve_pokemon(pokemon_list, evolution_map):
    evolved_pokemon_list = []
    for pokemon in pokemon_list:
        if pokemon in evolution_map:
            evolved_pokemon_list.append(evolution_map[pokemon])
        else:
            evolved_pokemon_list.append(pokemon)
    return evolved_pokemon_list

evolution_map = {
    "Poliwag": "Poliwhirl",
    "Bulbasaur": "Ivysaur",
    "Charmander": "Charmeleon",
    "Pidgey": "Pidgeotto",
    "Psyduck": "Golduck",
    "Abra": "Kadabra"
}

pokemon = ["Poliwag", "Pidgey", "Abra", "Charmander", "Bulbasaur", "Psyduck", "Goldeen"]

evolved_list = evolve_pokemon(pokemon, evolution_map)
print(evolved_list)