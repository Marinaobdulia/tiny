from PIL import Image, ImageFilter
import sys
import os

root_folder = str(sys.argv[1])

new_folder = str(sys.argv[2])
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

pokedex = os.listdir(root_folder)
print(pokedex)

for pokemon in pokedex:
    img = Image.open('.\\Pokedex\\'+pokemon)
    img.save(new_folder + pokemon[:-4] + '.png', 'png')
