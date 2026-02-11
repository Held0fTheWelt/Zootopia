import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


template_file = open("animals_template.html")

animals_data = load_data('animals_data.json')
output = ''  # define an empty string
for animal in animals_data:
    if 'name' in animal.keys():
        output += f"Name: {animal['name']}\n"
    if 'diet' in animal['characteristics'].keys():
        output += f"Diet: {animal['characteristics']['diet']}\n"
    if 'locations' in animal.keys():
        output += f"Location: {animal['locations'][0]}\n"
    if 'type' in animal['characteristics'].keys():
        output += f"Diet: {animal['characteristics']['type']}\n"

text = template_file.read().replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as output_file:
  output_file.write(text)