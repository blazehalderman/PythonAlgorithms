"""
  Write a function that takes in a non-empty string and that returns a boolean
  representing whether the string is a palindrome.
"""

def isPalindrome(string):
	#split strings in half
	if(len(string) == 1):
		return True
	length_s = len(string)
	if(length_s % 2 == 0):
		firsthalf, secondhalf = string[:(len(string)//2)], string[(len(string)//2):]
	else:
		firsthalf, secondhalf = string[:(len(string)//2)], string[((len(string))//2) + 1:]
	if(firsthalf == secondhalf[::-1]):
		return True
	else:
		return False

# or more simply...check the reverse of the string and if same, return true
