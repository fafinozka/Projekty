import time
import random
import sys

score = 0
yn = ['y', 'n']
Cont_game = True
print("welcome to Rock, Paper Scissors!")
time.sleep(1)

print("you will be presented with three options")
print("you choose Rock paper or scissors")
time.sleep(2)

print("the computer will decide randomly regardless of your choice")

begin = input("so, do you want to begin? y/n  ")
while Cont_game == True:
	if begin == 'y':
		print("[r]ock")
		print("[p]aper")
		print("[s]cissors")
		choice = input("Pick one: ")

	elif begin == 'n':
		print("see you soon!")
		sys.exit()
	if begin not in ('y', 'n'):
		print("[r]ock")
		print("[p]aper")
		print("[s]cissors")
		choice = input("Pick one: ")

	RPS = ['rock', 'paper', 'scissors']
	computer_choice = random.choice(RPS)
	if choice == 'r':
		choice = "rock"
		print("you chose rock!")
	elif choice == 'p':
		choice = "paper"
		print("you chose paper!")
	elif choice == 's':
		choice = "scissors"
		print("you chose scissors!")
	else:
		print("invalid entry, restarting")
		continue

	if choice not in ("rock", "paper", "scissors"):
		print("invalid entry! restarting...")
		continue



	if choice == "rock" and computer_choice == "scissors":
		print ("you won")
		score += 1
		print ("the computer chose:", computer_choice)
		cont = input("do you want to continue? y/n  ")
		if cont == 'y':
			print("your score is:", score)
			continue
		elif cont == 'n':
			print("your score was:", score)
			print("see you soon!")
			sys.exit()


	if choice == "rock" and computer_choice == "rock":
		print ("this ended with stalemate, restarting!")
		continue

	if choice == "rock" and computer_choice == "paper":
		print("you lost")
		score -= 1
		print("the computer chose:", computer_choice)
		cont = input("do you want to continue? y/n  ")
		if cont == 'y':
			print("your score is:", score)
			continue
		elif cont == 'n':
			print("your score was:", score)
			print("see you soon!")
			sys.exit()

	if choice == "paper" and computer_choice == "rock":
		print ("you won")
		score += 1
		print ("the computer chose:", computer_choice)
		cont = input("do you want to continue? y/n  ")
		if cont == 'y':
			print("your score is:", score)
			continue
		elif cont == 'n':
			print("your score was:", score)
			print("see you soon!")
			sys.exit()

	if choice == "paper" and computer_choice == "paper":
		print ("this ended with stalemate, restarting!")
		continue

	if choice == "paper" and computer_choice == "scissors":
		print("you lost")
		score -= 1
		print("the computer chose:", computer_choice)
		cont = input("do you want to continue? y/n  ")
		if cont == 'y':
			print("your score is:", score)
			continue
		elif cont == 'n':
			print("your score was:", score)
			print("see you soon!")
			sys.exit()


	if choice == "scissors" and computer_choice == "paper":
		print ("you won")
		score += 1
		print ("the computer chose:", computer_choice)
		cont = input("do you want to continue? y/n  ")
		if cont == 'y':
			print("your score is:", score)
			continue
		elif cont == 'n':
			print("your score was:", score)
			print("see you soon!")
			sys.exit()

	if choice == "scissors" and computer_choice == "scissors":
		print ("this ended with stalemate, restarting!")
		continue

	if choice == "scissors" and computer_choice == "rock":
		print("you lost")
		score -= 1
		print("the computer chose:", computer_choice)
		cont = input("do you want to continue? y/n  ")
		if cont == 'y':
			print("your score is:", score)
			continue
		elif cont == 'n':
			print("your score was:", score)
			print("see you soon!")
			sys.exit()

