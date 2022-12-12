import json


def populate_type_map():
    json_obj = load_type_map()
    type_list = json_obj["all"]

    for atk_type in type_list:
        for def_type in type_list:
            if def_type not in json_obj["types"][atk_type].keys():
                json_obj["types"][atk_type][def_type] = 1.0

    with open('data/types.json', 'w') as outfile:
        json.dump(json_obj, outfile, indent=4)


def load_type_map():
    json_obj = {}

    with open('data/types.json', 'r') as json_file:
        json_obj = json.load(json_file)

    return json_obj


def load_pokemon_data():
    json_obj = {}

    with open('data/moves.json', 'r') as json_file:
        json_obj = json.load(json_file)

    return json_obj["pokemon"]


def load_move_data():
    json_obj = {}

    with open('data/moves.json', 'r') as json_file:
        json_obj = json.load(json_file)

    return json_obj["moves"]


if __name__ == '__main__':
    populate_type_map()
