# wapp to read a string and find if its a palindrome
# string that  reads the same from --> and <--
# wow , mam, racecar, nitin, malayalam, madam, oyo, mom, dad

s1 = input(" enter a string ") # to read the input
r1 = s1[::-1]                        # reverse string using slice
if s1 == r1 :
	print("yes")
else:
	print("no")