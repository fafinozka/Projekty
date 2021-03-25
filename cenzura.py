import re
vstup = open ("vstup.txt", "rt")
a = vstup.read()
a2 = a.lower()

cenzura = open("cenzura.txt", "r")
content_cenzura = cenzura.read()
cenzura_list = content_cenzura.lower().split("\n")
cenzura.close()

for element in cenzura_list:
	a2 = (a2.replace(element, int(len(element)) * "*"))
print(a2)


