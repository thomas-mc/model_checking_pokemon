import sys
original_stdout = sys.stdout
f=open("pokemon_action2.txt",'w')
sys.stdout = f

# [p1_attack_pok1_move1_pok1] turn = 1 & (player1_pokemon_selection = 1 & player1_pokemon1_knocked = false) &(player2_pokemon_selection = 1 & player2_pokemon1_knocked = false) -> (player2_current_health' = max(0, player2_current_health - p1_pok1_move1_pok1_damage)) & (turn' = 3 - turn);


for first_loop in range(1,3):
    for second_loop in range(1,4):
        for third_loop in range(1,5):
            for fourth_loop in range(1,4):
                print("[player" + str(first_loop) + "_pokemon" + str(second_loop) + "_move" + str(third_loop) + "_attack_player" + str(3-first_loop) + "_pokemon" + str(fourth_loop) + "] turn = " + str(first_loop) + " & player" + str(first_loop) + "_current_health > 0 & (player" + str(first_loop) + "_pokemon_selection = " + str(second_loop) + " & player" + str(first_loop) + "_pokemon" + str(second_loop) + "_knocked = false) & (player" + str(3-first_loop) + "_pokemon_selection = " + str(fourth_loop) + " & player" + str(3-first_loop) + "_pokemon" + str(fourth_loop) + "_knocked = false) -> (player" + str(3-first_loop) + "_current_health' = max(0, player" + str(3-first_loop) + "_current_health - player" + str(first_loop) + "_pokemon" + str(second_loop) + "_move" + str(third_loop) + "_player" + str(3-first_loop) + "_pokemon" + str(fourth_loop) + "_damage)) & (turn' = 3 - turn);")
