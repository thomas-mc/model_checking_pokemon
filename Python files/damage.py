# Just a file to calculate damage for now
import random
import math

# parasect v nidoqueen
# solarbeam

level = 1
power = 120 /2
attack = 95 /2
defense = 87 /2

random = (random.randint(217,256))/255

print(random)

# just learned clefable is only fairy type from generation VI onwards, type=normal before that, so my pokedex is wrong

#move type is same as user's type
stab = 1.5

# grass, bug vs poison, ground
type_effective = 2 * 0.5 * 2

modifier = random * type_effective * stab

overall_damage = (((((2*level)/5)+2)*power*(attack/defense))/50) * modifier


print(overall_damage)
print(math.floor(overall_damage))