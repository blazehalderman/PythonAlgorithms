"""

  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Bubble Sort algorithm to sort the array.

"""
#Updated and working idea for bubble sort

def bubbleSort(array):
    # Write your code here.
	count = 0
	sort = False
	while not sort:
		sort = True
		for i in range(len(array) - 1 - count):
			if (array[i] > array[i + 1]):
				shift = array[i + 1]
				array[i + 1] = array[i]
				array[i] = shift
				sort = False
		count += 1
	return array
