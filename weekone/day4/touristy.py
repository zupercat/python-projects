city = input("The inquisitive zupercat asks you where you are going (name ONE place) ")

result = ""
attractions = input("The zupercat understands. She asks you to name some places to visit there. Keep typing...keep typing...When you're done type DONE and if the zupercat approves you can pass. ")
result += attractions

if (attractions) == "DONE":
	print("The zupercat welcomes you to",city+". Unfortunately, there doesn't seem to be any actual places for you to visit. Of course, if you enter a city/country with no actual places, perhaps you'll be interested in joining the zupercat's army.")

else:
	while True:
		attractions = input("The zupercat understands. She asks you to name some places to visit there. Keep typing...keep typing...When you're done type DONE and if the zupercat approves you can pass. ")
		if (attractions) == "DONE":
			break

		result += ", "+attractions
	print("The zupercat welcomes you to",city+". She may have never been there but she knows all about that place. She says that there is lots to see there like the army of grumpkins and cats she is raising...Just kidding. There are some actual places though, such as:",result+". ")
