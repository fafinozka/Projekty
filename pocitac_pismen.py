from time import sleep

import matplotlib.pyplot as plt
#"----------------------------------------------------------"

pismenka = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#"----------------------------------------------------------"

ABC_count = open("ABC_count.txt", "rt")
text = ABC_count.read()
text_malej = text.lower()


vysledek= {}
for znak in text_malej:
	if znak in vysledek:
		vysledek[znak]+=1
	else:
		vysledek[znak]=1


for i in (sorted(vysledek)):
	if i not in (pismenka):
		vysledek.pop(i)

total = 0
for i in vysledek:
	total += vysledek[i]
dict = {}
for i in (sorted(vysledek)):
	#print(f"Pismeno: {i}: {vysledek[i]}, {round(vysledek[i] / total * 100, 2)}%")
	dict[i] = {'cislo': vysledek[i], 'procento':round(vysledek[i] / total * 100, 2)}

left = range(len(dict))

for i in dict:
	height = [i]
#tick_label = dict[0]

#sleep (100)