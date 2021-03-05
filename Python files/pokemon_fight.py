import json

with open('pokedex_real.txt') as json_file:
    pokedex = json.load(json_file)

json_file.close()
# print(pokedex['1'])

for pokemon in pokedex:
    print(str(pokedex[pokemon]['name']) + " // Special: " + str(pokedex[pokemon]["base_stats"]["Special"]))
    # print(pokedex[pokemon]['base_stats']['Sp. Defense'])