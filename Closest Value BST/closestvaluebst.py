    """
  Write a function that takes in a Binary Search Tree (BST) and a target integer
  value and returns the closest value to that target value contained in the BST.

    """

def findClosestValueInBst(tree, target):
    # Write your code here.
	return findClosestValueInBstHelper(tree, target, float("inf"))
	
    pass

def findClosestValueInBstHelper(tree, target, closest):
	if (tree is None):
		return closest
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	if (target < tree.value):
		return findClosestValueInBstHelper(tree.left, target, closest)
	elif (target > tree.value):
		return findClosestValueInBstHelper(tree.right, target, closest)
	else:
		return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
