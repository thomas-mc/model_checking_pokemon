# Just a file to calculate damage for now
import random
import math

# parasect v nidoqueen
# solarbeam

level = 1
power = 120
attack = 65
defense = 100

random_no = (random.randint(217,256))/255


# just learned clefable is only fairy type from generation VI onwards, type=normal before that, so my pokedex is wrong

#move type is same as user's type
stab = 1

# grass v dragon, flying
type_effective = 0.5*0.5

modifier = random_no * type_effective * stab

overall_damage = ((((((2*level)/5)+2)*power*(attack/defense))/50)+2) * modifier


print(overall_damage)
print(math.floor(overall_damage))
# new = math.floor((((((2*1)/5)+2)*75*(130/95))/50) * random_no * 1.5 * 2)
# print(new)

# [player2_pokemon1_move3_attack_player1_pokemon1] turn = 2 & player2_current_health > 0 & (player2_pokemon_selection = 1 & player2_pokemon1_knocked = false) & (player1_pokemon_selection = 1 & player1_pokemon1_knocked = false) -> 1.0 :  (player1_current_health' = max(0, player1_current_health - 1)) & (turn' = 3 - turn) + 1 - 1.0 : (turn' = 3 - turn);