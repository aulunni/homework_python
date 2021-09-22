#def f(n):
	#print(n)
	#if n > 0:
		#f(n-1)
#f(50)
	
#def factorial(n):
	#if n == 0:
		#return 1
	#return factorial(n-1)*n
#print(factorial(7))
	
#n = int(input('Please print the number: '))
#print('The result is: ')

#for i in range(n - 1, 1, -1):
	#if (n % i == 0):
		#print(i)

a = int(input('Please print the number: '))
b = str(a)
c = []

for digit in b:
	c.append (int(digit))
print(c)
