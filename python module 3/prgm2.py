n = 1,2,3,4,5,6,7,8,9,10
count1 = 0
count2 = 0
for i in n :
	if i%2==0:
		count1+=1
	else :
		count2+=1
else :
	print("number are over in the series")
	print("odd numbers present in series is :",count2,"\neven numbers present in series is :",count1)
