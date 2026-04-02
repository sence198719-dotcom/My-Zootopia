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
    output+= f"Name: {animal['name']}\n"
    if "diet" in animal["characteristics"]:
        output += f"Diet: {animal['characteristics']['diet']}\n"
    if "locations" in animal:
        output += f"Locations: {animal['locations'][0]}\n"
    if "type" in animal["characteristics"]:
        output += f"Type: {animal['characteristics']['type']}\n"


print(output)

with open("animals_template.html", "r")as file:
    html_template = file.read()
print(html_template)

final_html=html_template.replace("__REPLACE_ANIMALS_INFO__",output)
print(final_html)

with open("animals.html", "w") as file:
    file.write(final_html)



