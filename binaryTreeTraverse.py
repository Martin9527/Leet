# Definition for a binary tree node.
class BTreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.result = []

	def inOrderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return
		if root.left:
			self.inOrderTraversal(root.left)
		self.result.append(root.val)
		if root.right:
			self.inOrderTraversal(root.right)
		return self.result

	def preOrderTraversal(self,root):
		if not root:
			return
		self.result.append(root.val)
		if root.left:
			self.preOrderTraversal(root.left)
		if root.right:
			self.preOrderTraversal(root.right)
		return self.result

	def postOrderTraversal(self,root):
		if not root:
			return
		if root.left:
			self.preOrderTraversal(root.left)
		if root.right:
			self.preOrderTraversal(root.right)
		self.result.append(root.val)
		return self.result

	def levelOrderTraversal(self,root):
		if not root:
			return
		tmp = [root]
		node = root
		while tmp:
			node = tmp.pop(0) 
			if node.left:
				tmp.append(node.left)
			if node.right:
				tmp.append(node.right)
			self.result.append(node.val)

		return self.result


	def flaten(self,root):
		#flaten this tree to a linked list in place
		if not root:
			return
		if root.left:
			self.flaten(root.left)
		if root.right:
			self.flaten(root.right)
		if root.left:
			pre = root.left
			while pre.right:
				pre = pre.right
			pre.right = root.right
			root.right = root.left
			root.left = None



if __name__ == '__main__':
	s = Solution()
	root = BTreeNode(1)
	root.left = BTreeNode(2)
	root.left.left = BTreeNode(3)
	root.left.right = BTreeNode(4)

	root.right = BTreeNode(5)
	root.right.right = BTreeNode(6)
	s.flaten(root)
	print 'root:: ',root.right.val,
	