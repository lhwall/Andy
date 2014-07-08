number = int(input("Please enter a number: "))
a = number % 3
b = number % 5
c = number % 15

if c == 0:
	print ("Fizzbuzz")
else:
	if a == 0:
		print ("Fizz")
	if b == 0:
		print ("Buzz")
