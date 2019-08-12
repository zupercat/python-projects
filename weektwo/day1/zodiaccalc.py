print("Hello and welcome to zupercat's almighty zodiac calculator.")

while True:
	birth_year = input("Please state your birth year.")
	if birth_year.isdigit():
		break

print("Calculating...Beep boop...")


def calculate_zodiac(birth_year):
	remainder = int(birth_year)%12
	if remainder == 0:
		zodiac = "Monkey"
	elif remainder == 1:
		zodiac = "Rooster"
	elif remainder == 2:
		zodiac = "Dog"
	elif remainder == 3:
		zodiac = "Pig"
	elif remainder == 4:
		zodiac = "Mouse"
	elif remainder == 5:
		zodiac = "Ox"
	elif remainder == 6:
		zodiac = "Tiger"
	elif remainder == 7:
		zodiac = "Rabbit"
	elif remainder == 8:
		zodiac = "Dragon"
	elif remainder == 9:
		zodiac = "Snake"
	elif remainder == 10:
		zodiac = "Horse"
	elif remainder == 11:
		zodiac = "Sheep"
	else:
		zodiac = "Non existant thing"
	return (zodiac)

def display_photo(animal):
	from PIL import Image
	if animal=="Monkey":
		im = Image.open("zodiacpic/monkey.png")
		im.show()
	elif animal=="Rooster":
		im = Image.open("zodiacpic/rooster.png")
		im.show()
	elif animal=="Dog":
		im = Image.open("zodiacpic/dog.png")
		im.show()
	elif animal=="Pig":
		im = Image.open("zodiacpic/pig.png")
		im.show()
	elif animal=="Mouse":
		im = Image.open("zodiacpic/mouse.png")
		im.show()
	elif animal=="Ox":
		im = Image.open("zodiacpic/ox.png")
		im.show()
	elif animal=="Tiger":
		im = Image.open("zodiacpic/tiger.png")
		im.show()
	elif animal=="Rabbit":
		im = Image.open("zodiacpic/rabbit.png")
		im.show()
	elif animal=="Dragon":
		im = Image.open("zodiacpic/dragon.png")
		im.show()
	elif animal=="Snake":
		im = Image.open("zodiacpic/snake.png")
		im.show()
	elif animal=="Horse":
		im = Image.open("zodiacpic/horse.png")
		im.show()
	elif animal=="Sheep":
		im = Image.open("zodiacpic/sheep.png")
		im.show()
	else:
		print("You don't have a photo.")



zodiac = calculate_zodiac(birth_year)
print(" ")
print("You are born in the year of the", zodiac+"!")
print(" ")
display_photo(zodiac)
