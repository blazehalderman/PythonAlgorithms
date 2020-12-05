"""
  Write a function that takes in a "special" array and returns its product sum.

  A "special" array is a non-empty array that contains either integers or other
  "special" arrays. The product sum of a "special" array is the sum of its
  elements, where "special" arrays inside it are summed themselves and then
  multiplied by their level of depth.
"""

#IN PROGRESS
def productSum(array):
	#loop through array
	# if item in array is an open parenthesis, multiply
	# and search for closing bracket
	# else add index values
	i = 0
	if(array[i][1] == "]"):
		#add total values in parenthesis
		temp_sum += array[i][0]
		#multiply to values in parenthesis
		i +=1
		sum_value *= temp_sum
		return sum_value
	if(array[i][0] == "["):
		temp_sum+= array[i][1]
		#sum_value += 
		productSum(array[i])
