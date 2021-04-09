import json
import sys
import random
import math
original_stdout = sys.stdout

with open('University Work\\model_checking_pokemon\\Python files\\teams_no_legends.txt') as json_file:
    teams = json.load(json_file)

json_file.close()

with open('University Work\\model_checking_pokemon\\Python files\\best_pokemon_best_moves.txt') as json_file:
    learnsets = json.load(json_file)

json_file.close()

with open('University Work\\model_checking_pokemon\\Python files\\best_moves_stats.json') as json_file:
    moves = json.load(json_file)

json_file.close()

with open('University Work\\model_checking_pokemon\\Python files\\pokedex_real.txt') as json_file:
    pokedex = json.load(json_file)

json_file.close()

with open('University Work\\model_checking_pokemon\\Python files\\type_effectiveness.txt') as json_file:
    type_effectiveness_list = json.load(json_file)

json_file.close()

poke_move_damage_list = []
poke_hp_variable_dict = {}
poke_speed_variable_dict = {}
team_matchups = {}
adversary_poke_hp_variable_dict = {}
adversary_poke_speed_variable_dict = {}
move_damage_variables = {}


for outer_team in teams:
    team_matchups[str(teams[outer_team])] = []
    for inner_team in teams:
        if outer_team != inner_team:
            team_matchups[str(teams[outer_team])].append(teams[inner_team])

for team in teams:
    poke_hp_variable_dict[str(teams[team])] = []
    adversary_poke_hp_variable_dict[str(teams[team])] = []
    count = 1
    for pokemon in teams[team]:
        for dex_pokemon in pokedex:
            if(pokedex[dex_pokemon]['name'] == pokemon):
                poke_hp_variable_dict[str(teams[team])].append("const int player1_pokemon{0}_hp = {1};".format(count,pokedex[dex_pokemon]['base_stats']['HP']))
                adversary_poke_hp_variable_dict[str(teams[team])].append("const int player2_pokemon{0}_hp = {1};".format(count,pokedex[dex_pokemon]['base_stats']['HP']))
        count+=1


for team in teams:
    poke_speed_variable_dict[str(teams[team])] = []
    adversary_poke_speed_variable_dict[str(teams[team])] = []
    count = 1
    for pokemon in teams[team]:
        for dex_pokemon in pokedex:
            if(pokedex[dex_pokemon]['name'] == pokemon):
                poke_speed_variable_dict[str(teams[team])].append("const int player1_pokemon{0}_speed = {1};".format(count,pokedex[dex_pokemon]['base_stats']['Speed']))
                adversary_poke_speed_variable_dict[str(teams[team])].append("const int player2_pokemon{0}_speed = {1};".format(count,pokedex[dex_pokemon]['base_stats']['Speed']))
        count+=1


teams_already_matched = {}
for team in teams:
    teams_already_matched[str(teams[team])] = {}
    for inner_team in teams:
        if str(teams[inner_team]) != str(teams[team]):
            teams_already_matched[str(teams[team])][str(teams[inner_team])] = False


live_stats = {}
live_damage_stats = {}
physical_move_types = ["Normal", "Fighting", "Flying", "Ground", "Rock", "Bug", "Ghost", "Poison"]
special_move_types = ["Water", "Grass", "Fire", "Ice", "Electric", "Psychic", "Dragon"]

for team in teams:
    team1_poke_count = 1
    for pokemon in teams[team]:
        live_stats['p1p{0}_pokemon'.format(team1_poke_count)] = pokemon
        team1_poke_count += 1
        for dex_pokemon in pokedex:
            if(pokedex[dex_pokemon]['name'] == pokemon):
                for counter in range(1,4):
                    live_stats['p1p{0}_attack'.format(counter)] = pokedex[dex_pokemon]['base_stats']['Attack']
                    live_stats['p1p{0}_defense'.format(counter)] = pokedex[dex_pokemon]['base_stats']['Defense']
                    live_stats['p1p{0}_special'.format(counter)] = pokedex[dex_pokemon]['base_stats']['Special']
                    live_stats['p1p{0}_type'.format(counter)] = pokedex[dex_pokemon]['type']
    for adversary_team in teams:
        if str(teams[adversary_team]) != str(teams[team]):
            if teams_already_matched[str(teams[adversary_team])][str(teams[team])] == False:
                teams_already_matched[str(teams[team])][str(teams[adversary_team])] = True
                team2_poke_count = 1
                for pokemon in teams[adversary_team]:
                    live_stats['p2p{0}_pokemon'.format(team2_poke_count)] = pokemon
                    team2_poke_count += 1
                    for dex_pokemon in pokedex:
                        if(pokedex[dex_pokemon]['name'] == pokemon):
                            for counter in range(1,4):
                                live_stats['p2p{0}_attack'.format(counter)] = pokedex[dex_pokemon]['base_stats']['Attack']
                                live_stats['p2p{0}_defense'.format(counter)] = pokedex[dex_pokemon]['base_stats']['Defense']
                                live_stats['p2p{0}_special'.format(counter)] = pokedex[dex_pokemon]['base_stats']['Special']
                                live_stats['p2p{0}_type'.format(counter)] = pokedex[dex_pokemon]['type']
                    
                for player_counter in range (1,3):
                    for pokemon_counter in range (1,4):
                        for move_counter in range(1,5):
                            for adv_pokemon_counter in range(1,4):
                                level = 1
                                random_var = (random.randint(217,256))/255
                                stab = 1
                                if player_counter == 1:
                                    power = moves[learnsets[live_stats['p1p{0}_pokemon'.format(pokemon_counter)]][move_counter-1]]['Power']
                                    attack = live_stats['p1p{0}_attack'.format(pokemon_counter)]
                                    defense = live_stats['p2p{0}_defense'.format(adv_pokemon_counter)]
                                    if moves[learnsets[live_stats['p1p{0}_pokemon'.format(pokemon_counter)]][move_counter-1]]['type'] in  live_stats['p1p{0}_type'.format(pokemon_counter)]:
                                        stab = 1.5
                                elif player_counter == 2:
                                    power = moves[learnsets[live_stats['p2p{0}_pokemon'.format(adv_pokemon_counter)]][move_counter-1]]['Power']
                                    attack = live_stats['p2p{0}_attack'.format(adv_pokemon_counter)]
                                    defense = live_stats['p1p{0}_defense'.format(adv_pokemon_counter)]
                                    if moves[learnsets[live_stats['p2p{0}_pokemon'.format(adv_pokemon_counter)]][move_counter-1]]['type'] in  live_stats['p2p{0}_type'.format(pokemon_counter)]:
                                        stab = 1.5

                                type_effectiveness = 1
                                if player_counter == 1:
                                    current_move_type = moves[learnsets[live_stats['p1p{0}_pokemon'.format(pokemon_counter)]][move_counter-1]]['type']
                                    for adv_poke_type in live_stats['p2p{0}_type'.format(adv_pokemon_counter)]:
                                        type_effectiveness = type_effectiveness * type_effectiveness_list[current_move_type][adv_poke_type]
                                    if current_move_type in special_move_types:
                                        attack = live_stats['p1p{0}_special'.format(pokemon_counter)]
                                        defense = live_stats['p2p{0}_special'.format(adv_pokemon_counter)]

                                elif player_counter == 2:
                                    current_move_type = moves[learnsets[live_stats['p2p{0}_pokemon'.format(pokemon_counter)]][move_counter-1]]['type']
                                    for adv_poke_type in live_stats['p1p{0}_type'.format(adv_pokemon_counter)]:
                                        type_effectiveness = type_effectiveness * type_effectiveness_list[current_move_type][adv_poke_type]
                                    if current_move_type in special_move_types:
                                        attack = live_stats['p2p{0}_special'.format(pokemon_counter)]
                                        defense = live_stats['p1p{0}_special'.format(adv_pokemon_counter)]

                                live_damage_stats['p{0}p{1}m{2}p{3}p{4}'.format(player_counter, pokemon_counter, move_counter, 3-player_counter, adv_pokemon_counter)] = math.floor(((((((2*level)/5)+2)*power*(attack/defense))/50)+2) * random_var * stab * type_effectiveness)


                # ---------------------UNCOMMENTING THIS CODE SPAMS FILES----------------------
                f=open("University Work\\model_checking_pokemon\\Prism_Models_No_Legends\\{0}_VERSUS_{1}.prism".format(team,adversary_team),'w')
                sys.stdout = f
                # -----------------------------------------------------------------------------

                print("smg")
                for pokemon_hp_var in poke_hp_variable_dict[str(teams[team])]:
                    print(pokemon_hp_var)
                for adv_pokemon_hp_var in adversary_poke_hp_variable_dict[str(teams[adversary_team])]:
                    print(adv_pokemon_hp_var)

                for pokemon_speed_var in poke_speed_variable_dict[str(teams[team])]:
                    print(pokemon_speed_var)
                for adv_pokemon_speed_var in adversary_poke_speed_variable_dict[str(teams[adversary_team])]:
                    print(adv_pokemon_speed_var)
                
                for player_counter in range(1,3):
                    for pokemon_counter in range(1,4):
                        for move_counter in range(1,5):
                            for adv_pokemon_counter in range(1,4):
                                print("const int player{0}_pokemon{1}_move{2}_player{3}_pokemon{4}_damage = {5};".format(player_counter, pokemon_counter, move_counter, 3-player_counter, adv_pokemon_counter, live_damage_stats['p{0}p{1}m{2}p{3}p{4}'.format(player_counter, pokemon_counter, move_counter, 3-player_counter, adv_pokemon_counter)]))

                for player_counter in range(1,3):
                    print("\nplayer player{0}".format(player_counter))
                    print("\t", end = " ")
                    for pokemon_counter in range(1,4):
                        print("[player{0}_select_pokemon{1}],".format(player_counter, pokemon_counter), end = " ")
                        for move_counter in range(1,5):
                            for adv_pokemon_counter in range(1,4):
                                if "[player{0}_pokemon{1}_move{2}_attack_player{3}_pokemon{4}]".format(player_counter, pokemon_counter, move_counter, 3-player_counter, adv_pokemon_counter) == "[player1_pokemon3_move4_attack_player2_pokemon3]" or "[player{0}_pokemon{1}_move{2}_attack_player{3}_pokemon{4}]".format(player_counter, pokemon_counter, move_counter, 3-player_counter, adv_pokemon_counter) == "[player2_pokemon3_move4_attack_player1_pokemon3]":
                                    print("[player{0}_pokemon{1}_move{2}_attack_player{3}_pokemon{4}]".format(player_counter, pokemon_counter, move_counter, 3-player_counter, adv_pokemon_counter))
                                else:
                                    print("[player{0}_pokemon{1}_move{2}_attack_player{3}_pokemon{4}],".format(player_counter, pokemon_counter, move_counter, 3-player_counter, adv_pokemon_counter), end = " ")
                    print("endplayer")
                
                print("\nmodule pokemon_battle")
                for player_counter in range(1,3):
                    print("\tplayer{0}_current_health : [0..highest_health_player{0}] init player{0}_pokemon1_hp;".format(player_counter))
                    print("\tplayer{0}_pokemon_selection : [1..3];".format(player_counter))

                print("\tturn : [0..2] init 0;")

                for player_counter in range(1,3):
                    for pokemon_counter in range(1,4):
                        print("\tplayer{0}_pokemon{1}_knocked : bool init false;".format(player_counter, pokemon_counter))

                print("\t[player1_select_pokemon1] player1_pokemon1_knocked = false & ((player1_pokemon_selection = 2 & player1_pokemon2_knocked = true) | (player1_pokemon_selection = 3 & player1_pokemon3_knocked = true)) -> (player1_pokemon_selection' = 1) & (player1_current_health' = player1_pokemon1_hp);")
                print("\t[player1_select_pokemon2] player1_pokemon2_knocked = false & ((player1_pokemon_selection = 1 & player1_pokemon1_knocked = true) | (player1_pokemon_selection = 3 & player1_pokemon3_knocked = true)) -> (player1_pokemon_selection' = 2) & (player1_current_health' = player1_pokemon2_hp);")
                print("\t[player1_select_pokemon3] player1_pokemon3_knocked = false & ((player1_pokemon_selection = 1 & player1_pokemon1_knocked = true) | (player1_pokemon_selection = 2 & player1_pokemon2_knocked = true)) -> (player1_pokemon_selection' = 3) & (player1_current_health' = player1_pokemon3_hp);")
                print("\t[player2_select_pokemon1] player2_pokemon1_knocked = false & ((player2_pokemon_selection = 2 & player2_pokemon2_knocked = true) | (player2_pokemon_selection = 3 & player2_pokemon3_knocked = true)) -> (player2_pokemon_selection' = 1) & (player2_current_health' = player2_pokemon1_hp);")
                print("\t[player2_select_pokemon2] player2_pokemon2_knocked = false & ((player2_pokemon_selection = 1 & player2_pokemon1_knocked = true) | (player2_pokemon_selection = 3 & player2_pokemon3_knocked = true)) -> (player2_pokemon_selection' = 2) & (player2_current_health' = player2_pokemon2_hp);")
                print("\t[player2_select_pokemon3] player2_pokemon3_knocked = false & ((player2_pokemon_selection = 1 & player2_pokemon1_knocked = true) | (player2_pokemon_selection = 2 & player2_pokemon2_knocked = true)) -> (player2_pokemon_selection' = 3) & (player2_current_health' = player2_pokemon3_hp);")

                print("\t[player1_pokemon1_knocked_out] player1_current_health = 0 & turn = 1 & player1_pokemon_selection = 1 -> (player1_pokemon1_knocked' = true) & (turn' = 0);")
                print("\t[player1_pokemon2_knocked_out] player1_current_health = 0 & turn = 1 & player1_pokemon_selection = 2 -> (player1_pokemon2_knocked' = true) & (turn' = 0);")
                print("\t[player1_pokemon3_knocked_out] player1_current_health = 0 & turn = 1 & player1_pokemon_selection = 3 -> (player1_pokemon3_knocked' = true) & (turn' = 0);")
                print("\t[player2_pokemon1_knocked_out] player2_current_health = 0 & turn = 2 & player2_pokemon_selection = 1 -> (player2_pokemon1_knocked' = true) & (turn' = 0);")
                print("\t[player2_pokemon2_knocked_out] player2_current_health = 0 & turn = 2 & player2_pokemon_selection = 2 -> (player2_pokemon2_knocked' = true) & (turn' = 0);")
                print("\t[player2_pokemon3_knocked_out] player2_current_health = 0 & turn = 2 & player2_pokemon_selection = 3 -> (player2_pokemon3_knocked' = true) & (turn' = 0);")

                for oc in range(3):
                    oc += 1
                    for ic in range(3):
                        ic += 1
                        print("\t[set_turn] turn = 0 & player1_pokemon_selection = " + str(oc) + " & player2_pokemon_selection = " + str(ic) + " & player1_pokemon" + str(oc) + "_knocked = false & player2_pokemon" + str(ic) + "_knocked = false & player1_pokemon" + str(oc) + "_speed > player2_pokemon" + str(ic) + "_speed -> (turn' = 1);")
                        print("\t[set_turn] turn = 0 & player1_pokemon_selection = " + str(oc) + " & player2_pokemon_selection = " + str(ic) + " & player1_pokemon" + str(oc) + "_knocked = false & player2_pokemon" + str(ic) + "_knocked = false & player1_pokemon" + str(oc) + "_speed = player2_pokemon" + str(ic) + "_speed -> 0.5 : (turn' = 1) + 0.5 : (turn' = 2);")
                        print("\t[set_turn] turn = 0 & player1_pokemon_selection = " + str(oc) + " & player2_pokemon_selection = " + str(ic) + " & player1_pokemon" + str(oc) + "_knocked = false & player2_pokemon" + str(ic) + "_knocked = false & player1_pokemon" + str(oc) + "_speed < player2_pokemon" + str(ic) + "_speed -> (turn' = 2);")

                for player_counter in range(1,3):
                    for pokemon_counter in range(1,4):
                        for move_counter in range(1,5):
                            for adv_pokemon_counter in range(1,4):
                                if moves[learnsets[live_stats['p1p{0}_pokemon'.format(pokemon_counter)]][move_counter-1]]['Accuracy'] == 100:
                                    print("\t[player{0}_pokemon{1}_move{2}_attack_player{3}_pokemon{4}] turn = {0} & player{0}_current_health > 0 & (player{0}_pokemon_selection = {1} & player{0}_pokemon{1}_knocked = false) & (player{3}_pokemon_selection = {4} & player{3}_pokemon{4}_knocked = false) -> (player{3}_current_health' = max(0, player{3}_current_health - {5})) & (turn' = 3 - turn);".format(player_counter,pokemon_counter,move_counter,3-player_counter,adv_pokemon_counter,live_damage_stats['p{0}p{1}m{2}p{3}p{4}'.format(player_counter, pokemon_counter, move_counter, 3-player_counter, adv_pokemon_counter)]))
                                else:
                                    print("\t[player{0}_pokemon{1}_move{2}_attack_player{3}_pokemon{4}] turn = {0} & player{0}_current_health > 0 & (player{0}_pokemon_selection = {1} & player{0}_pokemon{1}_knocked = false) & (player{3}_pokemon_selection = {4} & player{3}_pokemon{4}_knocked = false) -> {6} :  (player{3}_current_health' = max(0, player{3}_current_health - {5})) & (turn' = 3 - turn) + 1 - {6} : (turn' = 3 - turn);".format(player_counter,pokemon_counter,move_counter,3-player_counter,adv_pokemon_counter,live_damage_stats['p{0}p{1}m{2}p{3}p{4}'.format(player_counter, pokemon_counter, move_counter, 3-player_counter, adv_pokemon_counter)],(moves[learnsets[live_stats['p1p{0}_pokemon'.format(pokemon_counter)]][move_counter-1]]['Accuracy'])/100))




                print("endmodule")
                print('label "player1_wins" = (player1_pokemon1_knocked = false | player1_pokemon2_knocked = false | player1_pokemon3_knocked = false) & (player2_pokemon1_knocked = true & player2_pokemon2_knocked = true & player2_pokemon3_knocked = true);')
                print('label "player2_wins" = (player2_pokemon1_knocked = false | player2_pokemon2_knocked = false | player2_pokemon3_knocked = false) & (player1_pokemon1_knocked = true & player1_pokemon2_knocked = true & player1_pokemon3_knocked = true);')
                print("formula highest_health_player1 = max(player1_pokemon1_hp, player1_pokemon2_hp, player1_pokemon3_hp);")
                print("formula highest_health_player2 = max(player2_pokemon1_hp, player2_pokemon2_hp, player2_pokemon3_hp);")