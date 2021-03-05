import json

with open('learnset.txt') as json_file:
    learnset = json.load(json_file)

json_file.close()
count = 0

overall_learnset = []
for pokemon in learnset:
    for move in learnset[pokemon]:
        overall_learnset.append(move)

overall_learnset_unique = set(overall_learnset)


#format: move_stats = {"move_name":{type: "move_type", power: number, accuracy: number}}
move_stats = {}

for move in overall_learnset_unique:
    move_stats[move] = {"type": "Normal", "Power": 0, "Accuracy": 0}


# print(move_stats)

with open("moves_stats.json", "a") as outfile:
    json.dump(move_stats, outfile, indent = 2)

# json_moves = json.dumps(move_stats)
# print(json_moves)