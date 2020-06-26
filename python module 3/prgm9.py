#prgm on to check is palindrome are not
n = int(input("enter a number:"))
rev = 0
while(n != 0):
	remi = n%10
	rev = rev*10+remi
	n = n//10
print("reverse of the number:",rev)
if n==rev :
	print(n,"is a palindrome ")
else :
	print("it is not a palindrome")
