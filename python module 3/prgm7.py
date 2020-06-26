n = int(input("enter a number from starting to get odd :"))
m = int(input("enter a number upto odd one :"))
print("odd numbers is between the range you entered :")
for i in range(n,m) :
	if (i%2 != 0) :
		print(i)