import json
import copy

with open('University Work\\model_checking_pokemon\\Python files\\pokedex_real.txt') as json_file:
    pokedex = json.load(json_file)

json_file.close()
# print(pokedex['1'])
# "base_stats": {"HP": 45, "Attack": 49, "Defense": 49, "Special": 65, "Speed": 45}

for pokemon in pokedex:
    pokedex[pokemon]["base_stats"]["Total"] = pokedex[pokemon]["base_stats"]["HP"] + pokedex[pokemon]["base_stats"]["Attack"] + pokedex[pokemon]["base_stats"]["Defense"] + pokedex[pokemon]["base_stats"]["Special"] + pokedex[pokemon]["base_stats"]["Speed"]
    print(str(pokedex[pokemon]['name']) + " // Total: " + str(pokedex[pokemon]["base_stats"]["Total"]))

best_in_class = []
# best_in_class format = [[pokemon_index, pokemon_name, [pokemon_type]], ]

# type is always a list of strings, even with 1 element

print("")
print("")
print("-----------------------------------------------------------------")
print("SORTED BY THE TOTAL STAT")
print("-----------------------------------------------------------------")
print("")
print("")
for pokemon in pokedex:
    found = False
    for element in best_in_class:
        if set(element[2]) == set(pokedex[pokemon]['type']):
            # print(element[2])
            found = True
            # print(pokedex[pokemon]["base_stats"]["Total"])
            # print(element[0])
            # print(pokemon)
            # print(pokedex[element[0]]["base_stats"]["Total"])
            if pokedex[pokemon]["base_stats"]["Total"] > pokedex[element[0]]["base_stats"]["Total"]:
                best_in_class.remove(element)
                best_in_class.append([pokemon, pokedex[pokemon]["name"], pokedex[pokemon]['type']])
    if found == False:
        best_in_class.append([pokemon, pokedex[pokemon]["name"], pokedex[pokemon]['type']])

count = 0
for item in best_in_class:
    item.append(pokedex[item[0]]["base_stats"]["Total"])
    print("Name: " + str(item[1]) + " // Type: " + str(item[2]) + " // Total: " + str(pokedex[item[0]]["base_stats"]["Total"]))
    count += 1
    print(count)

sorted_list_total = copy.deepcopy(best_in_class)

l = len(sorted_list_total)
for i in range(0,l):
    for j in range(0, l-i-1):
        if (sorted_list_total[j][3] < sorted_list_total[j+1][3]):
            temp = sorted_list_total[j]
            sorted_list_total[j] = sorted_list_total[j+1]
            sorted_list_total[j+1] = temp


print(sorted_list_total)

with open('University Work\\model_checking_pokemon\\Python files\\type_effectiveness.txt') as json_file1:
    type_effectiveness = json.load(json_file1)

json_file1.close()

# for item in type_effectiveness:
#     print(item)
# print(type_effectiveness[0])

# over type product
print("")
print("")
print("-----------------------------------------------------------------")
print("SORTED BY THE PRODUCT OF TYPE EFFECTIVENESS")
print("-----------------------------------------------------------------")
print("")
print("")
product = 1
for pok in sorted_list_total:
    for pok_type in pok[2]:
        for effect_type in type_effectiveness:
            if pok_type == effect_type:
                for inner_type in type_effectiveness[pok_type]:
                    product = product * type_effectiveness[pok_type][inner_type]
    pok.append({"type_product":product})
    product = 1

sorted_list_type_effectiveness_product = copy.deepcopy(sorted_list_total)
l = len(sorted_list_type_effectiveness_product)
for i in range(0,l):
    for j in range(0, l-i-1):
        if (sorted_list_type_effectiveness_product[j][4]["type_product"] < sorted_list_type_effectiveness_product[j+1][4]["type_product"]):
            temp = sorted_list_type_effectiveness_product[j]
            sorted_list_type_effectiveness_product[j] = sorted_list_type_effectiveness_product[j+1]
            sorted_list_type_effectiveness_product[j+1] = temp

print(sorted_list_type_effectiveness_product)
print("")
print("")
print("-----------------------------------------------------------------")
print("SORTED BY THE NUMBER OF ADVANTAGES-DISADVANTAGES")
print("-----------------------------------------------------------------")
print("")
print("")
# counting number of type advantages and disadvantages
sorted_list_type_advantages_sum_minus_disadvantages = copy.deepcopy(sorted_list_type_effectiveness_product)
advantages = 0
disadvantages = 0
for outer_poke in sorted_list_type_advantages_sum_minus_disadvantages:
    for inner_poke in sorted_list_type_advantages_sum_minus_disadvantages:
        for outer_poke_type in outer_poke[2]:
            for inner_poke_type in inner_poke[2]:
                for outer_effect_type in type_effectiveness:
                    if outer_poke_type == outer_effect_type:
                        for current_type in type_effectiveness[outer_poke_type]:
                            if type_effectiveness[outer_poke_type][current_type] == 2:
                                advantages += 1
                            elif type_effectiveness[outer_poke_type][current_type] < 1:
                                disadvantages += 1
    outer_poke.append({"difference":advantages-disadvantages})
    outer_poke.append({"advantages":advantages,"disadvantages":disadvantages})
    advantages = 0
    disadvantages = 0

l = len(sorted_list_type_advantages_sum_minus_disadvantages)
for i in range(0,l):
    for j in range(0, l-i-1):
        if (sorted_list_type_advantages_sum_minus_disadvantages[j][5]["difference"] < sorted_list_type_advantages_sum_minus_disadvantages[j+1][5]["difference"]):
            temp = sorted_list_type_advantages_sum_minus_disadvantages[j]
            sorted_list_type_advantages_sum_minus_disadvantages[j] = sorted_list_type_advantages_sum_minus_disadvantages[j+1]
            sorted_list_type_advantages_sum_minus_disadvantages[j+1] = temp
print(sorted_list_type_advantages_sum_minus_disadvantages)


print("")
print("")
print("-----------------------------------------------------------------")
print("SORTED BY THE NUMBER OF ADVANTAGES")
print("-----------------------------------------------------------------")
print("")
print("")

l = len(sorted_list_type_advantages_sum_minus_disadvantages)
for i in range(0,l):
    for j in range(0, l-i-1):
        if (sorted_list_type_advantages_sum_minus_disadvantages[j][6]["advantages"] < sorted_list_type_advantages_sum_minus_disadvantages[j+1][6]["advantages"]):
            temp = sorted_list_type_advantages_sum_minus_disadvantages[j]
            sorted_list_type_advantages_sum_minus_disadvantages[j] = sorted_list_type_advantages_sum_minus_disadvantages[j+1]
            sorted_list_type_advantages_sum_minus_disadvantages[j+1] = temp
print(sorted_list_type_advantages_sum_minus_disadvantages)



print("")
print("")
print("-----------------------------------------------------------------")
print("SORTED BY THE NUMBER OF DISADVANTAGES")
print("-----------------------------------------------------------------")
print("")
print("")

l = len(sorted_list_type_advantages_sum_minus_disadvantages)
for i in range(0,l):
    for j in range(0, l-i-1):
        if (sorted_list_type_advantages_sum_minus_disadvantages[j][6]["disadvantages"] > sorted_list_type_advantages_sum_minus_disadvantages[j+1][6]["disadvantages"]):
            temp = sorted_list_type_advantages_sum_minus_disadvantages[j]
            sorted_list_type_advantages_sum_minus_disadvantages[j] = sorted_list_type_advantages_sum_minus_disadvantages[j+1]
            sorted_list_type_advantages_sum_minus_disadvantages[j+1] = temp
print(sorted_list_type_advantages_sum_minus_disadvantages)



print("")
print("")
print("-----------------------------------------------------------------")
print("SORTED BY THE SUM OF THE TYPE MULTIPLIERS")
print("-----------------------------------------------------------------")
print("")
print("")

# sum of the type effectiveness multipliers
sorted_list_type_sum_multipliers = copy.deepcopy(sorted_list_type_advantages_sum_minus_disadvantages)
type_sum = 0
for pok in sorted_list_type_sum_multipliers:
    for pok_type in pok[2]:
        for effect_type in type_effectiveness:
            if pok_type == effect_type:
                for inner_type in type_effectiveness[pok_type]:
                    type_sum += type_effectiveness[pok_type][inner_type]
    pok.append({"type_sum":type_sum})
    type_sum = 0

l = len(sorted_list_type_sum_multipliers)
for i in range(0,l):
    for j in range(0, l-i-1):
        if (sorted_list_type_sum_multipliers[j][7]["type_sum"] < sorted_list_type_sum_multipliers[j+1][7]["type_sum"]):
            temp = sorted_list_type_sum_multipliers[j]
            sorted_list_type_sum_multipliers[j] = sorted_list_type_sum_multipliers[j+1]
            sorted_list_type_sum_multipliers[j+1] = temp
print(sorted_list_type_sum_multipliers)
print("")
print("")
print("-----------------------------------------------------------------")
print("SORTED BY A COMBINATION OF TOTAL STATS AND TYPE EFFECTIVENESS")
print("-----------------------------------------------------------------")
print("")
print("")
# Type combo, calculation down below
sorted_list_total_type_combo = copy.deepcopy(sorted_list_type_sum_multipliers)
combo_type_effectiveness = 1
for outer_pokemon in sorted_list_total_type_combo:
    outer_pokemon.append({"combo_ratio_list":[]})
    for inner_pokemon in sorted_list_total_type_combo:
        for outer_poke_type in outer_pokemon[2]:
            for inner_poke_type in inner_pokemon[2]:
                for effect_type in type_effectiveness:
                    if outer_poke_type == effect_type:
                        for current_type in type_effectiveness[outer_poke_type]:
                            if current_type == inner_poke_type:
                                combo_type_effectiveness = combo_type_effectiveness * type_effectiveness[outer_poke_type][current_type]
        # calculation = (attacking total/defending total) * type effectiveness
        outer_pokemon[8]["combo_ratio_list"].append((outer_pokemon[3]/(inner_pokemon[3]))*combo_type_effectiveness)
        combo_type_effectiveness = 1

counter = 0
for item in sorted_list_total_type_combo:
    for ratio in item[8]["combo_ratio_list"]:
        if ratio > 1:
            counter += 1
    item[8]["dominant_count"] = counter
    counter = 0


l = len(sorted_list_total_type_combo)
for i in range(0,l):
    for j in range(0, l-i-1):
        if (sorted_list_total_type_combo[j][8]["dominant_count"] < sorted_list_total_type_combo[j+1][8]["dominant_count"]):
            temp = sorted_list_total_type_combo[j]
            sorted_list_total_type_combo[j] = sorted_list_total_type_combo[j+1]
            sorted_list_total_type_combo[j+1] = temp
print(sorted_list_total_type_combo)


print("")
print("")
print("-----------------------------------------------------------------")
print("SORTED BY TOTAL STAT * PRODUCT EFFECTIVENESS")
print("-----------------------------------------------------------------")
print("")
print("")
# Type combo, calculation down below
sorted_list_total_effect_product = copy.deepcopy(sorted_list_total_type_combo)

for pokemon in sorted_list_total_effect_product:
    pokemon.append({"combo_total_type_product":pokemon[3]*pokemon[4]["type_product"]})
    # pokemon[9]["combo_total_type_product"] = pokemon[3]*pokemon[4]["type_product"]


l = len(sorted_list_total_effect_product)
for i in range(0,l):
    for j in range(0, l-i-1):
        if (sorted_list_total_effect_product[j][9]["combo_total_type_product"] < sorted_list_total_effect_product[j+1][9]["combo_total_type_product"]):
            temp = sorted_list_total_effect_product[j]
            sorted_list_total_effect_product[j] = sorted_list_total_effect_product[j+1]
            sorted_list_total_effect_product[j+1] = temp
print(sorted_list_total_effect_product)


print("")
print("")
print("-----------------------------------------------------------------")
print("SORTED BY TOTAL STAT + TYPE ADVANTAGES COUNT")
print("-----------------------------------------------------------------")
print("")
print("")
# Type combo, calculation down below
sorted_list_total_plus_advantages = copy.deepcopy(sorted_list_total_effect_product)

for pokemon in sorted_list_total_plus_advantages:
    pokemon.append({"combo_total_plus_advantages":pokemon[3]+pokemon[6]["advantages"]})
    # pokemon[9]["combo_total_type_product"] = pokemon[3]*pokemon[4]["type_product"]


l = len(sorted_list_total_plus_advantages)
for i in range(0,l):
    for j in range(0, l-i-1):
        if (sorted_list_total_plus_advantages[j][10]["combo_total_plus_advantages"] < sorted_list_total_plus_advantages[j+1][10]["combo_total_plus_advantages"]):
            temp = sorted_list_total_plus_advantages[j]
            sorted_list_total_plus_advantages[j] = sorted_list_total_plus_advantages[j+1]
            sorted_list_total_plus_advantages[j+1] = temp
print(sorted_list_total_plus_advantages)


print("")
print("")
print("-----------------------------------------------------------------")
print("SORTED BY TOTAL STAT - TYPE DISADVANTAGES COUNT")
print("-----------------------------------------------------------------")
print("")
print("")
# Type combo, calculation down below
sorted_list_total_minus_disadvantages = copy.deepcopy(sorted_list_total_plus_advantages)

for pokemon in sorted_list_total_minus_disadvantages:
    pokemon.append({"combo_total_minus_disadvantages":pokemon[3]-pokemon[6]["disadvantages"]})
    # pokemon[9]["combo_total_type_product"] = pokemon[3]*pokemon[4]["type_product"]


l = len(sorted_list_total_minus_disadvantages)
for i in range(0,l):
    for j in range(0, l-i-1):
        if (sorted_list_total_minus_disadvantages[j][11]["combo_total_minus_disadvantages"] < sorted_list_total_minus_disadvantages[j+1][11]["combo_total_minus_disadvantages"]):
            temp = sorted_list_total_minus_disadvantages[j]
            sorted_list_total_minus_disadvantages[j] = sorted_list_total_minus_disadvantages[j+1]
            sorted_list_total_minus_disadvantages[j+1] = temp
print(sorted_list_total_minus_disadvantages)