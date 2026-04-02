import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)
animals = load_data('animals_data.json')
print(animals)

for animal in animals:
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



