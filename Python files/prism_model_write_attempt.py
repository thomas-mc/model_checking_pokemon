import sys
original_stdout = sys.stdout
f=open("python_write_pokemon.txt",'w')
sys.stdout = f

pokemon = {}
default_stats = {"hp":None,"attack":None,"defence":None,"special":None,"speed":None,"total":None,"turn":None}
# pokemon["eevee"] = default_stats.copy()
pokemon["eevee"] = {"hp":None,"attack":None,"defence":None,"special":None,"speed":None,"total":None,"turn":None}
# pokemon["machop"] = default_stats.copy
pokemon["machop"] = {"hp":None,"attack":None,"defence":None,"special":None,"speed":None,"total":None,"turn":None}

#was going to try and iterate through but realized they have different stats so we'll see
# for pokem in pokemon.keys():
#     pokemon[pokem][hp] = 55


pokemon["eevee"]["hp"] = 55
pokemon["eevee"]["attack"] = 11 #1/5 of actual attack for now
pokemon["eevee"]["defence"] = 50
pokemon["eevee"]["special"] = 65
pokemon["eevee"]["speed"] = 55
pokemon["eevee"]["total"] = 280
pokemon["eevee"]["turn"] = 1

pokemon["machop"]["hp"] = 70
pokemon["machop"]["attack"] = 16 #1/5 of actual attack for now
pokemon["machop"]["defence"] = 50
pokemon["machop"]["special"] = 35
pokemon["machop"]["speed"] = 35
pokemon["machop"]["total"] = 270
pokemon["machop"]["turn"] = 2


print("mdp\n")

for pokem in pokemon.keys():
    print("const int " + str(pokem) + "_attack = " + str(pokemon[pokem]["attack"]) + ";\n")
    print("const int " + str(pokem) + "_defence = " + str(pokemon[pokem]["defence"]) + ";\n")
    print("const int " + str(pokem) + "_special = " + str(pokemon[pokem]["special"]) + ";\n")
    print("const int " + str(pokem) + "_speed = " + str(pokemon[pokem]["speed"]) + ";\n")
    print("const int " + str(pokem) + "_total = " + str(pokemon[pokem]["total"]) + ";\n" + "\n")

print("module pokemon_battle\n")
for pokem in pokemon.keys():
    print("\t" + str(pokem) + "_hp : [-20.." + str(pokemon[pokem]["hp"]) + "] init " + str(pokemon[pokem]["hp"]) + ";\n\n")

print("\tturn : [0..2];")
print("\t[random_start]	turn = 0 -> 0.5 : (turn' = 1) + 0.5 : (turn' = 2);")

for pokem in pokemon.keys():
    for pokem_inner in pokemon.keys():
        if pokem_inner == pokem:
            continue
        else:
            print("\t[" + str(pokem) + "_attack_" + str(pokem_inner) + "] turn = " + str(pokemon[pokem]["turn"]) + " & " + str(pokem) + "_hp > 0 & " + str(pokem_inner) + "_hp > 0->\n")
            print("\t\t1/2 : (" + str(pokem_inner) + "_hp' = " + str(pokem_inner) + "_hp - " + str(pokem) + "_attack) & (turn' = " + str(pokemon[pokem_inner]["turn"]) + ") +\n")
            print("\t\t1/2 : (turn'="+ str(pokemon[pokem_inner]["turn"]) + ");\n\n")

print("endmodule\n")

for pokem in pokemon.keys():
    for pokem_inner in pokemon.keys():
        if pokem_inner == pokem:
            continue
        else:
            print('label "' + str(pokem) + '_wins" = ' + str(pokem) + '_hp > 0 & ' + str(pokem_inner) + '_hp < 1;\n')


sys.stdout = original_stdout
f.close()