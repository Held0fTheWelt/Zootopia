import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


template_file = open("animals_template.html")

animals_data = load_data('animals_data.json')
output = ""
for animal in animals_data:
    output += '<li class="cards__item">\n'

    if 'name' in animal:
        output += f"Name: {animal['name']}<br/>\n"

    if 'characteristics' in animal:
        chars = animal['characteristics']
        if 'diet' in chars:
            output += f"Diet: {chars['diet']}<br/>\n"

    if 'locations' in animal and animal['locations']:
        output += f"Location: {animal['locations'][0]}<br/>\n"

    if 'characteristics' in animal:
        chars = animal['characteristics']
        if 'type' in chars:
            output += f"Type: {chars['type']}<br/>\n"

    output += "</li>\n"

text = template_file.read().replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w") as output_file:
  output_file.write(text)