    """
  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.

    """


def isValidSubsequence(array, sequence):
    # Write your code here.
	j = 0
	for i in range(len(array)):
		
		if(sequence[j] == array[i]):
			print(sequence[j])
			print(array[i])
			j+=1
			if(len(sequence) == j):
				return True
			continue
		else:
			continue
	return False
    pass