vstup = open("vstup.txt", "rt")
a=vstup.read()

cenzura = open("cenzura.txt", "r")
content_cenzura = cenzura.read()
cenzura_list = content_cenzura.split("\n")
cenzura.close()

for element in cenzura_list:
	a=(a.replace(element, int(len(element)) * "*"))
print(a)