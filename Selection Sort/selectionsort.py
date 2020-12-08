"""
  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Selection Sort algorithm to sort the array.
"""

def selectionSort(array):
    # Write your code here.
	for i in range(len(array)):
		j = i + 1
		for j in range(len(array) - 1):
			if(array[i] < array[j]):
				swap(i, j, array)
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
