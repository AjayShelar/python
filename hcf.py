#HCF 
#take two numbers as input

a=input()
b=input()

for i in range(1,100):
	if(a%i==0) and (b%i==0):
		hcf=i

print("hcf is",i)
