import json

def load_data(file_path):
    """
    Loads a JSON file
    :param file_path:
    :return: data of the json file
    """
    with open (file_path, "r") as handle:
        return json.load(handle)


def print_animals():
    """
    prints the Name, diet, first location from list, type for each animal
    """
    animals_data = load_data('animals_data.json')

    for animal in animals_data:
        if "name" in animal:
            print(f"Name: {animal['name']}")

        characteristics = animal.get("characteristics", {})
        if "diet" in characteristics:
            print(f"Diet: {characteristics['diet']}")

        locations = animal.get("locations", [])
        if locations:
            print(f"Location: {locations[0]}")

        if "type" in characteristics:
            print(f"Type: {characteristics['type']}")

        print()

print_animals()