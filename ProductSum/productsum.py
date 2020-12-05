"""
  Write a function that takes in a "special" array and returns its product sum.

  A "special" array is a non-empty array that contains either integers or other
  "special" arrays. The product sum of a "special" array is the sum of its
  elements, where "special" arrays inside it are summed themselves and then
  multiplied by their level of depth.
"""

def productSum(array, depth=1):
	sum_num = 0
	for i in range(len(array)):
		print(array[i])
		if(type(array[i]) is list):
			sum_num += productSum(array[i], depth + 1)
		else:
			sum_num += array[i]
	return (depth * sum_num)
