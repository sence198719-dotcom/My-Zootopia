import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)
animals_data = load_data('animals_data.json')


for animal in animals_data:
    name=animal["name"]
    print(name)
    characteristics= animal["characteristics"]
    if "diet" in characteristics:
        print(f"Diet: {characteristics['diet']}")
    if "locations" in animal:
        print(f"Locations: {animal['locations'][0]}")
    if "type" in characteristics:
        print(f"Type: {characteristics['type']}")
    print()

output=""
for animal in animals_data:
    output+= f'<li class="cards__item">'
    output+= f'<div class="card__title">{animal['name']}</div><br>\n'
    output+= f'<p class="card__text">'
    if "diet" in animal["characteristics"]:
        output += f"<strong>Diet:</strong>{animal['characteristics']['diet']}<br>\n"
    if "locations" in animal:
        output += f"<strong>Locations:</strong> {animal['locations'][0]}<br>\n"
    if "type" in animal["characteristics"]:
        output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br>\n"
    output += "</p></li>"

print(output)

with open("animals_template.html", "r")as file:
    html_template = file.read()
print(html_template)

final_html=html_template.replace("__REPLACE_ANIMALS_INFO__",output)
print(final_html)

with open("animals.html", "w") as file:
    file.write(final_html)



