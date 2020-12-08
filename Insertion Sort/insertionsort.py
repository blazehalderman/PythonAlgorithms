"""
  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Insertion Sort algorithm to sort the array.
"""


def insertionSort(array):
    #keep track of sorted numbers
	#keep track of continuation
	for i in range(1, len(array)):
		j = i
		while(j > 0 and array[j] < array[j - 1]):
			swap(j, j - 1, array)
			j -= 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
