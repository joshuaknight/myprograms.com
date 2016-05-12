
def fact():
	user =  int(input('Enter the Number of Factorial:'))
	i = 1
	m= user
	lis = []
	for i in range(user):
		lis.append(i * m )
		user -= 1 
		print lis


fact()
