#create list of elementsto be sort

list = [5,9,3,1,2,8,4,7,6]



for i in range(len(list)):
	for x in range(len(list)-1,i,-1):
		if ((list[x-1]) > list[x]):
			temp = list[x]
			list[x] = list[x-1]
			list[x-1] = temp
	

print(list)
