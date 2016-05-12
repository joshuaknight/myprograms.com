def leap():
	year = int(input("Enter a Year:"))
	if (year % 4 ) == 0 & ( year % 100) == 0 & (year % 400 ) == 0:
		print year," is a leap Year"
	else:
		print year," is not a leap year"

def prime():
	num = int(input('Enter a num'))
	if num > 1:
		for i in range(2,num):
			if num % i == 0:
				print num," is not a prime number"
				break
		else:
			print num," is a prime number"
	else:
		print " not a prime Number"		

def fact(x):
	fact = 1
	for i in range(1,x + 1):
		fact *= i
	print fact



fact(5)
prime()
leap()		

