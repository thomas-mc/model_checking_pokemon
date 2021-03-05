import sys
original_stdout = sys.stdout
f=open("move_damage.txt",'w')
sys.stdout = f
import random

# const int player1_pokemon1_move1_player2_pokemon1_damage = 1

for ic in range(3):
    ic += 1
    for oc in range(4):
        oc += 1
        for iic in range(3):
            iic += 1
            print("const int player1_pokemon" + str(ic) + "_move" + str(oc) + "_player2_pokemon" + str(iic) + "_damage = " + str(random.randint(4,11)) + ";")

for ic in range(3):
    ic += 1
    for oc in range(4):
        oc += 1
        for iic in range(3):
            iic += 1
            print("const int player2_pokemon" + str(ic) + "_move" + str(oc) + "_player1_pokemon" + str(iic) + "_damage = " + str(random.randint(1,11)) + ";")

