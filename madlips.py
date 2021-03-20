#na zacatku se zepta na pet podstatnych jmen, pet pridavnych, pet sloves. Nasledne se nahoodne slozi pet vet,ktere musi byt kazda jako jeden string. Pak se to spoji a bude z toho pribeh jako jeden string
#POTOOM SE PROVEDE SPOCITANI KOLIK JE JAKYCH PISMENEK V CELEM TEXTU.
import random


#slice_0 = slice(1)
#slice_1 = slice(2)
#slice_2 = slice(3)
#slice_3 = slice(4)
#slice_4 = slice(5)


noun_number = 0
noun_list = []
adjective_number = 0
adjective_list = []
verb_number = 0
verb_list = []

while noun_number < 5:
	noun = input(f"please enter {noun_number+1}. noun : ")
	noun_list.append(noun)
	noun_number += 1

while adjective_number < 5:
	adjective = input(f"please enter {adjective_number+1}. adjective: ")
	adjective_list.append(adjective)
	adjective_number += 1

while verb_number < 5:
	verb = input(f"please enter {verb_number+1}. verb: ")
	verb_list.append(verb)
	verb_number += 1

random.shuffle(noun_list)
random.shuffle(adjective_list)
random.shuffle(verb_list)


print(adjective_list[0].capitalize(), noun_list[0], verb_list[0],'.')
print(adjective_list[1].capitalize(), noun_list[1], verb_list[1],'.')
print(adjective_list[2].capitalize(), noun_list[2], verb_list[2],'.')
print(adjective_list[3].capitalize(), noun_list[3], verb_list[3],'.')
print(adjective_list[4].capitalize(), noun_list[4], verb_list[4],'.')