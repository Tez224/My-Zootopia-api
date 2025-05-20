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
    output = ""

    for animal in animals_data:
        output += "<li class='cards__item'>"

        if "name" in animal:
            output += f"<div class='card__title'>{animal['name']}</div>"

        output += f"<p class='card__text'>"

        characteristics = animal.get("characteristics", {})
        if "diet" in characteristics:
            output += f"<strong>Diet:</strong> {characteristics['diet']}<br/>"

        locations = animal.get("locations", [])
        if locations:
            output += f"<strong>Location:</strong> {locations[0]}<br/>"

        if "type" in characteristics:
            output += f"<strong>Type:</strong> {characteristics['type']}<br/>"
        output += "</p>"
        output += "</li>"
    return output

def get_html():
    with open("animals_template.html", "r") as file:
        return file.read()



def replace_html_placeholder():
    html = get_html()
    animals_output = print_animals()

    animal_html =  html.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    output_file = "animals.html"

    with open(output_file, "w") as file:
        file.write(animal_html)

    print("HTML content has been written to", output_file)

replace_html_placeholder()