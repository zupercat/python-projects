c = 0

while c == 0:
	location = input("The zupercat demands to know where you are going next. Will it be school, mall, or the gym? ")
	if location == "school":
		print("The zupercat is feeling particularly kind today. She reminds you to bring your homework, avoid Mr.Riches and wishes you good luck in maths class.")
		n = 1
		break
	elif location == "mall":
		print("The zupercat is jealous of you but she grudgingly reminds you to bring some money with you. Oh...she didn't say whose money.")
		n = 1
		break
	elif location == "gym":
		print("The zupercat says nothing but she brings you your water bottle and her towel. Welp...MUST.OBEY.ZUPERCAT!")
		n = 1
		break
	else:
		print("The zupercat hisses at you menacingly. She forbids you to go to",location,"and says that if you go without her permission she will eat your lunch.")