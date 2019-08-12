# GCI Excercise #
while True:
	n_marks = input("Please enter your number. ")

	if n_marks.isdigit():
		break


n = int(n_marks)
result = 1
for i in range(1,n+1):
	result = result*i
print (result)