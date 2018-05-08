
# The txt file needs to be in utf-8 for it to be read.

f = open('madlib.txt', 'r')
madlib = f.read()

print("------------------The MadLib Game------------------")
v_str = 'VERB ENDING IN “ING”'
b_str = "PART OF THE BODY"
p_str = "PLACE"
madlib = madlib.replace("PLURAL NOUN", "plural_n ")
madlib = madlib.replace("NOUN", "nnn")
madlib = madlib.replace(v_str, "vvv ")
madlib = madlib.replace(b_str, "bbb ")
madlib = madlib.replace(p_str, "ppp ")


madlib_split = madlib.split()
adj_count = 0
noun_count = 0
plural_noun_count = 0
game_count = 0
verb_ing_count = 0
plant_count = 0
body_part_count = 0
place_count = 0
num_count = 0


#this changes the adjectives
for word in madlib_split:
	if word == "ADJECTIVE":
		adj_count += 1 
	
	if word == "plural_n":
		plural_noun_count += 1

	if word == "nnn":
		noun_count += 1

	if word == "GAME":
		game_count += 1

	if word == "vvv":
		verb_ing_count += 1
	
	if word == "bbb":
		body_part_count += 1

	if word == "PLANT":
		plant_count += 1

	if word == "ppp":
		place_count += 1

	if word == "NUMBER":
		num_count += 1


for i in range(game_count):
	game = input("Please type the name of a game: ")
	madlib = madlib.replace("GAME",game,1)
	print("")

for i in range(adj_count):
	adj = input("Please type an adjective: ")
	madlib = madlib.replace("ADJECTIVE",adj,1)
	print("")

for i in range(verb_ing_count):
	verb_ing = input('Please type a verb ending with "ing": ')
	madlib = madlib.replace('vvv',verb_ing,1)
	print("")

for i in range(plant_count):
	plant = input('Please type the name of a plant: ')
	madlib = madlib.replace('PLANT',plant,1)
	print("")

for i in range(noun_count):
	noun = input("Please type a noun: ")
	madlib = madlib.replace("nnn",noun,1)
	print("")

for i in range(plural_noun_count):
	plural_noun = input("Please type a plural noun: ")
	madlib = madlib.replace("plural_n",plural_noun,1)
	print("")

for i in range(body_part_count):
	body_part = input("Please type the name of a body part: ")
	madlib = madlib.replace("bbb",body_part,1)
	print("")

for i in range(place_count):
	place = input("Please type the name of a place: ")
	madlib = madlib.replace("ppp",place,1)
	print("")

for i in range(num_count):
	number = input("Please type a number: ")
	madlib = madlib.replace("NUMBER",number,1)
	print("")
	
plural_noun_space = plural_noun + " "
madlib = madlib.replace(" .", ".")
madlib = madlib.replace(" ,", ",")
madlib = madlib.replace(plural_noun_space, plural_noun)


print("---------------------MadLib---------------------")
print(madlib)




		


































