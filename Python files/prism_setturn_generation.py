import sys
original_stdout = sys.stdout
f=open("select_pokemon.txt",'w')
sys.stdout = f

# [player1_select_pokemon1] player1_pokemon1_knocked = false & ((player1_pokemon_selection = 2 & player1_pokemon2_knocked) | (player1_pokemon_selection = 3 & player1_pokemon3_knocked)) -> (player1_pokemon_selection' = 1) & (player1_current_health' = player1_pokemon1_hp)


for oc in range(3):
    oc += 1
    for ic in range(3):
        ic += 1
        print("[set_turn] turn = 0 & player1_pokemon_selection = " + str(oc) + " & player2_pokemon_selection = " + str(ic) + " & player1_pokemon" + str(oc) + "_knocked = false & player2_pokemon" + str(ic) + "_knocked = false & player1_pokemon" + str(oc) + "_speed > player2_pokemon" + str(ic) + "_speed -> (turn' = 1);")
        print("[set_turn] turn = 0 & player1_pokemon_selection = " + str(oc) + " & player2_pokemon_selection = " + str(ic) + " & player1_pokemon" + str(oc) + "_knocked = false & player2_pokemon" + str(ic) + "_knocked = false & player1_pokemon" + str(oc) + "_speed = player2_pokemon" + str(ic) + "_speed -> 0.5 : (turn' = 1) + 0.5 : (turn' = 2);")
        print("[set_turn] turn = 0 & player1_pokemon_selection = " + str(oc) + " & player2_pokemon_selection = " + str(ic) + " & player1_pokemon" + str(oc) + "_knocked = false & player2_pokemon" + str(ic) + "_knocked = false & player1_pokemon" + str(oc) + "_speed < player2_pokemon" + str(ic) + "_speed -> (turn' = 2);")