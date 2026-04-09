import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)
data= load_data('animals_data.json')

def show_animal_details(data):
    for animal in data:
        print(f"{animal['name']}")

        if "diet" in animal["characteristics"]:
            print(f"Diet: {animal['characteristics']['diet']}")

        if "type" in animal["characteristics"]:
            print(f"Type: {animal['characteristics']['type']}")

        if "locations" in animal and len(animal["locations"]) > 0:
            print(f"Location: {animal['locations'][0]}")
        print()

def serialize_animal(animal_obj):
    output = ""
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<p class="card__text">\n'

    if "diet" in animal_obj["characteristics"]:
        output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"

    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"

    if "type" in animal_obj["characteristics"]:
        output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n"

    output += "</p>\n"
    output += "</li>\n"
    return output


def main():
    data = load_data("animals_data.json")

    show_animal_details()

    output = ""
    for animal in data:
        output += serialize_animal(animal)

    with open("animals_template.html", "r") as file:
        html_template = file.read()
        final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as file:
        file.write(final_html)

if __name__ == "__main__":
    main()








