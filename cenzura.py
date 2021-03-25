import re
vstup = open ("vstup.txt", "rt")
text = vstup.read()
text_malej = text.lower()

cenzura = open("cenzura.txt", "r")
content_cenzura = cenzura.read()
cenzura_list = content_cenzura.lower().split("\n")
cenzura.close()

text_cenzura = text_malej

for element in cenzura_list:
	text_cenzura = (text_cenzura.replace(element, int(len(element)) * "*"))
print(text_cenzura)


vysledek={}
for element in cenzura_list:
	text_krajeni = text_malej
	pozice_abs=0
	pole=[]
	while True:
		pozice = text_krajeni.find(element)
		if pozice == -1:
			vysledek[element]=pole
			break
		else:
			#print(f"Na pozici: {pozice_abs} je slovo: {element} ")
			text_krajeni = text_krajeni[(pozice+len(element)):]

			pozice_abs += pozice
			pole.append(pozice_abs)

for i in vysledek:
	print(i, vysledek[i])