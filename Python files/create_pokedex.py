import json

pokedex = {}

with open('Python files\\pokedex1.json', encoding="utf-8") as json_file1:
    data = json.load(json_file1)
    for p in data:
        for thing in p['type']:
            print(thing)
            if thing == "Fairy":
                print("HELLO----------------------------------")
                print(p['type'])
                p['type'].remove("Fairy")
                if "Normal" not in p['type']:
                    p['type'].append("Normal")
        pokedex[p['id']] = {'name':p['name']['english'],'type':p['type'],'base_stats':p['base'],'weaknesses':None}

json_file1.close()


with open('Python files\\pokedex.json') as json_file:
    data = json.load(json_file)
    for p in data['pokemon']:
        for item in pokedex:
            if item == p['id']:
                pokedex[item]['weaknesses'] = p['weaknesses']
                
json_file.close()

# for item in pokedex:
#     print(pokedex[item])

with open('pokedex_no_fairy.txt', 'w') as outfile:
    json.dump(pokedex, outfile)
