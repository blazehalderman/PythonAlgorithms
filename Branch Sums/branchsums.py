    """
  Write a function that takes in a Binary Tree and returns a list of its branch
  sums ordered from leftmost branch sum to rightmost branch sum.
    """

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sum_array = []
    branchSumsHelper(root, 0, 0, sum_array)
    return sum_array

def branchSumsHelper(current, sum_temp, i, sum_array):
	if (current is None):
		return
	sum_temp += current.value
	if (current.left == None and current.right == None):
		sum_array.append(sum_temp)
		sum_temp = 0
		i += 1
	branchSumsHelper(current.left, sum_temp, i, sum_array)
	branchSumsHelper(current.right, sum_temp, i, sum_array)   