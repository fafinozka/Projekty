import random, time
import sys


#obrazky hangmana
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#word list
words = ["time","year","people","way","day","man","thing","woman","life","child","world","school","state","family","student","group","country","problem",\
 "hand","part","place","case","week","company","system","program","question","work","government","number","night","point","home",\
"water","room","mother","area","money","story","fact","month","lot","right","study","book","eye","job","word","business","issue","side","kind",\
"head","house","service","friend","father","power","hour","game","line","end","member","law","car","city",\
"community","name","president","team","minute","idea","kid","body","information","back", "parent",\
"face", "others","level","office","door","health","person","art","war","history",\
"party","result","change","morning","reason","research", "girl", "guy","moment"\
, "air", "teacher", "force", "education"]


#guess limit
g_limit = 7
#guesses
g_attempt = 0
#abeceda
alphabet = "abcdefghijklmnopqrstuvwxyz"
#nahodne slovo vylosovano
SecretWord = random.choice(words)
#delka slova
length_word = len(SecretWord)
#list open word
OpenWord=[]
#string open word
OpenWordStr=""
Used_Num=[]
#zjistime kolik ma nahodne slovo pismen a nahradime je podtrzitkama ktere vytiskneme
for element in range(0,len(SecretWord)):
	OpenWord.append('_')

#privitani a vysvetleni
input("Welcome to word guesser® press enter to continue!")
time.sleep(1)

print("Your task is to guess letters that make up a word.")
time.sleep(1)

print("You have 7 tries to guess a word after that, you lose or win.")
time.sleep(1)

print("Have fun!")
time.sleep(1)
#oznamime ze nahodne slovo bylo vybrano
print("Random word has been selected")
time.sleep(1)
#oznamime uzivateli jak je slovo dlouhe
print("your word has ", length_word, "letters")
ChciPokracovat = True
#zeptame se uzivatele na pismenko do te doby nez mu dojdou pokusy
while ChciPokracovat:
	if g_attempt == g_limit:
		print("you lost! the word was,", SecretWord)
		break
	guess = input("Please guess a letter: ")
	if not Used_Num.count(guess) > 0:
		Used_Num.append(guess)
		Used_Num = sorted(Used_Num)
	print(Used_Num)
#pokud pismenko neni v nasi vydefinovane abecede, oznamime to uzivateli, odecteme mu pokus a vyzveme aby to napsal spravne napiseme kolik ma zbyvajicich pokusu a ukazeme mu hangmana
	if guess not in alphabet:
		print("your letter is not in the a-z alphabet. Try again.")
		g_attempt += 1
		print("you have", g_limit - g_attempt, "guesses remaining")
		print(HANGMANPICS[g_attempt-1])
		continue
#pokud se pismenko vyskytuje v tajnem slove oskenujeme pismenko po pismenku a pozice kde jsou podtrzitka nahradime
#spravnym pismenem
	if guess in SecretWord:
		for element in range(0,len(SecretWord)):
			if guess == SecretWord[element]:
				OpenWord[element]=guess
		OpenWordStr = ''
#pokud po skenovani odhalime ze uzivatel odhalil cele slovo tak mu vypiseme ze vyhral
		for element in range(0,len(OpenWord)):
			OpenWordStr += OpenWord[element]
		print (OpenWordStr)
		if OpenWordStr == SecretWord:
			print ("congratulations, you won!")
			exit(0)
#kdyz pismenko neni v tajnem slove tak odecteme uzivateli pocet zbyvajicich pokusu a vytiskneme mu hangmana
	else:
		print("Letter given is not in the secret word!")
		g_attempt += 1
		print("you have", g_limit - g_attempt, "guesses remaining")
		print(HANGMANPICS[g_attempt - 1])


