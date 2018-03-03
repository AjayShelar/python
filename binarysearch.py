#create a list
b = [8,2,5,6,3,16,7,9,1,0]
b.sort()

print(b)
num = 5
i = len(b)/2
if(b[i] == num):
	print(num,'is at',i+1,'th position in list')
else:
	while(b[i]> num):
		i = i - 1
	while(b[i]< num):
		i = i + 1

print(num,'is at',i+1,'th position in list')
