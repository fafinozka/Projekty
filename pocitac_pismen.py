"----------------------------------------------------------"
pismenka = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
			'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

pismenka_pocet = {"a": 0,"b": 0,"c": 0,"d": 0,"e": 0,"f": 0,"g": 0,"h": 0,"i": 0,"j": 0,
"k": 0,"l": 0,"m": 0,"n": 0,"o": 0,"p": 0,"q": 0,"r": 0,"s": 0,"t": 0,"u": 0,"v": 0,"w": 0,"x": 0,"y": 0,"z": 0,
"A": 0,"B": 0,"C": 0,"D": 0,"E": 0,"F": 0,"G": 0,"H": 0,"I": 0,"J": 0,"K": 0,"L": 0,"M": 0,"N": 0,"O": 0,"P": 0,"Q": 0,"R": 0,"S": 0,"T": 0,"U": 0,
"V": 0,"W": 0,"X": 0,"Y": 0,"Z": 0}

"----------------------------------------------------------"

ABC_count = open("ABC_count.txt", "rt")
text = ABC_count.read()

for pismenka in text:
	
print(pismenka_pocet)