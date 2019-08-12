import random
import time

print("Welcome to guess zupercat's number (nice version)! You are the chosen one :D The zupercat says you must enter a number between 1-10 or you shall feel the wrath of the mighty zupercat. You have 3 chances to guess it right! But don't worry, we won't hurt you (too much) if you get it wrong :)")


def get_number_from_user():
	while True:
		n_marks = input("State your number. ")

		if n_marks.isdigit():
			break
	n = int(n_marks)
	return n

g = 0
correct_number = random.randint(1,10)

for g in range(1,4,1):
	n = get_number_from_user()
	if n == int(correct_number):
		print("That's correct! The zupercat will spare you and your lunch.")
		break
	elif g == 3:
		print("You lose, the answer was,",str(correct_number)+". But don't be upset! You have won a free night at zupercat's hotel (dungeon)! :D")
	elif n == 5:
		print("Hey! That's one of zupercat's favourite numbers!")
		time.sleep(2)
		print("But you're still wrong :)")
		time.sleep(1)
	elif n == 71:
		print("That's the serial number of zupercat's mars base! How did yo...")
		time.sleep(2)
		print("Where's the memory wiper?")
		time.sleep(1)
	elif n == 1976:
		print("Welcome to the hotel California...")
		time.sleep(2)
		print("Such a lovely place, such a lonely place... *epic guitar playing* ")
		time.sleep(2)
	elif n > 10:
		print("Oops! Looks like you just wasted a chance lol. That's what happens when you disobey the zupercat. You can only enter a number between 1-10!")
	else:
		print("Incorrect!")