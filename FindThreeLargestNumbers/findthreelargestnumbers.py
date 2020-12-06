"""
  Write a function that takes in an array of at least three integers and,
  without sorting the input array, returns a sorted array of the three largest
  integers in the input array.
"""

def findThreeLargestNumbers(array):
	#loop through array
	larg = []
	big = 0
	n = 3
	while(n > 0):
		for i in range(len(array)):
			if(array[i] is not None):
				if(array[i] > big and findNum(larg, array[i])):
					big = array[i]
		larg.append(big)
		big = 0
		n-=1
	temp = larg[0]
	larg[0] = larg[2]
	larg[2] = temp
	larg = numCheck(larg)
	return(larg)

def numCheck(array):
	i = 2
	while(i > 0):
		temp = array[i]
		print(temp)
		i-=1
		if(array[i] == 0):
			array[i] = temp
			temp = 0
	return array
			
def findNum(array, num):
	for item in array:
		if(item == num):
			return False
	return True
