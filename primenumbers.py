num = 0
prime = []
while num:
	if num > 1:
		for i in range(2,num):
			if (num%i) == 0:
				print(num,"is not a prime number")
				print(i,"times",num//i,"is",num)
				break
			
		else :
			print(num,"is prime")
			prime.extend([num])


	else :
		print(num,"is not a prime number")
	
	num = num + 1

print("prime numbers are :",prime)