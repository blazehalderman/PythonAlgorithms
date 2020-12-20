"""
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.
"""
def threeNumberSum(array, targetSum):
	found_sum = []
	array.sort()
    for i in range(len(array) - 2):
		for j in range(1, len(array)):
			for k in range(len(array) - 1, ):
				if(array[i] + array[j] + array[k] == targetSum):
					found_sum.append([array[i], array[j], array[k]])
					j += 1
					k -= 1
	return(found_sum)
