"""
  Implement the depthFirstSearch method on the
  Node class, which takes in an empty array, traverses the tree
  using the Depth-first Search approach, stores all of the nodes' names in the input array, and returns
  it.
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
		array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
		return array
