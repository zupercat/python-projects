name = input("State your name ")
print("Hello,",name,"let's see if you should spoil yourself and go to the concert... ")
print("Please answer with yes or no in the following questions or the super cat shall make you her slave for the rest of your days. ")
rain_tonight = input("Raining outside? ")
fifty_dollars = input("Got more than 50 dollars? ")
one_going = input("Is Cat One going? ")
two_going = input("Is Cat Two going? ")

if fifty_dollars == "Yes" and rain_tonight == "No" and one_going == "Yes" or two_going == "Yes":
	print("Beep boop calculating...the unicorn kitty says you are allowed to go to the concert so I suppose you ought to go (MUST.OBEY.CATS)");
else: 
	print("The super cat has spoken...do not go to the concert or you shall suffer a gruesome death at her paws.");