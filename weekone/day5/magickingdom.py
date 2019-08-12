# magic kingdom #


# defining functions #
def get_number_from_user(s):
	while True:
		n_marks = input(s)

		if n_marks.isdigit():
			break
	n = int(n_marks)
	return n


def calculate_pythagoras(n,m):
	c_squared = int(n)**2+int(m)**2
	c = c_squared**(0.5)
	return (c)

def square_area(c):
	three = calculate_pythagoras
	area = c * c
	return (area)

def the_answer_paragraph(n,m,c,area):
	print("From zupercat's triangular hotel with the sides of",str(n),"and",str(m)+", there lies the holy square of the grammar police station with equal sides of",str(c),"and an area of",str(area))


# stuffies #
one = get_number_from_user_one("Enter the first side of zupercat's triangular hotel. ")
two = get_number_from_user_one("Enter the second side of zupercat's triangular hotel. ")
three = calculate_pythagoras(one,two)
four = square_area(three)
the_answer_paragraph(one,two,three,four)
