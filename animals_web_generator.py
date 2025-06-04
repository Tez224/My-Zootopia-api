import requests
import json

def load_data():
    """
    Loads a JSON file
    :param file_path: The path to the JSON file to load.
    :return: The data of the json file, or an empty list if an error occurred.
    """
    try:
        name = 'Fox'
        api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)

        response = requests.get(api_url, headers={'X-Api-Key': 'FAv8L5/agkSfDxafl0Fpew==ce3t7X5VNkLcee2E'})

        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            print("Error:", response.status_code, response.text)

    except Exception:
        print("An error occurred.")
        return []

def get_skin_types(animal_data):
    """
    Retrieves a list of all unique skin types from the animal data.
    :param animal_data: The list of animals to extract skin types from.
    :return: List of skin types.
    """
    skin_types = set()
    for animal in animal_data:
        if "characteristics" in animal and "skin_type" in animal["characteristics"]:
            skin_types.add(animal["characteristics"]["skin_type"])
    return list(skin_types)


def serialize_animal(animal):
    """
    Serializes a single animal's data into HTML format.
    :param animal: The animal dictionary to serialize.
    :return: The HTML representation of the animal.
    """
    output = "<li class='cards__item'>"
    if "name" in animal:
        output += f"<div class='card__title'>{animal['name']}</div>"
    output += f"<p class='card__text'>"
    output += "<ul>"

    characteristics = animal.get("characteristics", {})
    if "diet" in characteristics:
        output += f"<li><strong>Diet:</strong> {characteristics['diet']}</li>"

    locations = animal.get("locations", [])
    if locations:
        output += f"<li><strong>Location:</strong> {locations[0]}</li>"

    if "type" in characteristics:
        output += f"<li><strong>Type:</strong> {characteristics['type']}</li>"

    if "skin_type" in characteristics:
        output += f"<li><strong>Skin Type:</strong> {characteristics['skin_type']}</li>"

    output += "</ul>"
    output += "</div>"
    output += "</li>"
    return output


def generate_html():
    """
    Generates the HTML content by replacing the placeholder with actual animal data.
    :return: The generated HTML content as a string.
    """
    html = get_html()
    animals_data = load_data()
    animals_output = ""

    for animal in animals_data:
        animals_output += serialize_animal(animal)

    return html.replace("__REPLACE_ANIMALS_INFO__", animals_output)


def get_html():
    """
    Reads the template HTML file and returns its content.
    :return: The template HTML content.
    """
    try:
        with open("animals_template.html", "r") as file:
            return file.read()
    except Exception as e:
        print(f"An error occurred while reading the template file: {e}")
        return ""


def write_html_to_file(html_content):
    """
    Writes the generated HTML content to a file.
    :param html_content: The HTML content to write to the file.
    """
    try:
        with open("animals.html", "w") as file:
            file.write(html_content)
        print("HTML content has been written to animals.html")
    except Exception as e:
        print(f"Something went wrong while writing the HTML to the file: {e}")


def main():
    """
    Main function to execute the tasks.
    """
    html_content = generate_html()  # Generate HTML content
    if html_content:
        write_html_to_file(html_content)  # Write the generated HTML to a file


if __name__ == "__main__":
    main()