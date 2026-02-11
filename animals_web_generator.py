import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def serialize_animal(animal_obj):
    animal_output = ""
    animal_output += '<li class="cards__item">\n'

    if 'name' in animal:
        animal_output += f'<div class="card__title">{animal['name']}</div>\n'
        animal_output += '<div class="card__text"><ul>'
        if 'characteristics' in animal:
            chars = animal['characteristics']
            if 'diet' in chars:
                animal_output += f"<li><strong>Diet:</strong> {chars['diet']}</li>\n"

        if 'locations' in animal and animal['locations']:
            animal_output += f"<li><strong>Location:</strong> {animal['locations'][0]}</li>\n"

        if 'characteristics' in animal:
            chars = animal['characteristics']
            if 'type' in chars:
                animal_output += f"<li><strong>Type:</strong> {chars['type']}</li>\n"
        animal_output += '</ul></div>'
    animal_output += "</li>\n"
    return animal_output

template_file = open("animals_template.html")

animals_data = load_data('animals_data.json')
output = ""
for animal in animals_data:
    output += serialize_animal(animal)

text = template_file.read().replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w") as output_file:
  output_file.write(text)