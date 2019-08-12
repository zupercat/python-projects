# GCI Excercise #

# Defining Functions #
def get_number_from_user():
	while True:
		n_marks = input("Please enter your number. ")

		if n_marks.isdigit():
			break
	n = int(n_marks)
	return n


def calculate_factorial(n):
	result = 1
	for i in range(1,n+1):
		result = result*i
	print (result)

# Code with functions #
number_from_user = get_number_from_user()
calculate_factorial(number_from_user)