#Initial idea for bubble sort(sort once)

def bubbleSort(array):
    # Write your code here.
	for i in range(len(array) - 1):
		if (array[i] > array[i + 1]):
			shift = array[i + 1]
			array[i + 1] = array[i]
			array[i] = shift
	return array
