vstup = open("vstup.txt", "rt")
a=vstup.read()

cenzura = open("cenzura.txt", "r")
content_cenzura = cenzura.read()
cenzura_list = content_cenzura.split(",")
cenzura.close()
print(a.replace(cenzura_list[0], len(cenzura_list[0]) * "*"))