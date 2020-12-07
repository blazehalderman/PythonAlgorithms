"""
  Write a function that takes in an array of at least three integers and,
  without sorting the input array, returns a sorted array of the three largest
  integers in the input array.
"""

def findThreeLargestNumbers(array):
	#define array for finite list
	larg = [None, None, None]
	#search array first largest value or current num greater then stored num
	#move to next index in reverse and repeat steps until no more largest value
	for i in range(len(array)):
		if(larg[2] == None or array[i] > larg[2]):
			checkValues(larg, 2, array[i])
		elif(larg[1] == None or array[i] > larg[1]):
			checkValues(larg, 1, array[i])
		elif(larg[0] == None or array[i] > larg[0]):
			checkValues(larg, 0, array[i])
	return(larg)

#shifts index values up to current index
def checkValues(array, index, num):
	for i in range(index + 1):
		if (i == index):
			array[i] = num
		else:
			array[i] = array[i + 1]
