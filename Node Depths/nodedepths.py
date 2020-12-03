"""
  The distance between a node in a Binary Tree and the tree's root is called the
  node's depth.
"""

def nodeDepths(root):
	return(nodeDepthsHelper(root, 0))

def nodeDepthsHelper(root, depth_count):
	if(root == None):
		return 0
	depth_count += nodeDepthsHelper(root.left, depth_count + 1) + nodeDepthsHelper(root.right, depth_count + 1)
	return depth_count
		

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
