import json

from models.moves import Move


def populate_type_map() -> None:
    """Reads in the data/types.json file and ensures all types have a value for all types"""
    json_obj = load_type_map()
    type_list = json_obj["all"]

    for atk_type in type_list:
        for def_type in type_list:
            if def_type not in json_obj["types"][atk_type].keys():
                json_obj["types"][atk_type][def_type] = 1.0

    with open('data/types.json', 'w') as outfile:
        json.dump(json_obj, outfile, indent=4)


def load_type_map() -> list:
    """Reads the data/types.json file and returns a list of json objects"""
    json_obj = {}

    with open('data/types.json', 'r') as json_file:
        json_obj = json.load(json_file)

    return json_obj


def load_pokemon_data() -> list:
    """Reads the data/pokemon.json file and returns a list of json objects"""
    json_obj = {}

    with open('data/pokemon.json', 'r') as json_file:
        json_obj = json.load(json_file)

    return json_obj["pokemon"]


def load_move_data() -> list:
    """Reads the data/moves.json file and returns a list of json objects"""
    json_obj = {}

    with open('data/moves.json', 'r') as json_file:
        json_obj = json.load(json_file)

    return json_obj["moves"]


def generate_moves() -> list:
    """Generates a list of Move objects from the data/moves.json file"""
    json_list = load_move_data()

    moves = []

    for move in json_list:
        moves.append(Move.fromJSON(json_list[move]))

    return moves
