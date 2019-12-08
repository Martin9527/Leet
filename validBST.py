# -*- coding: UTF-8 -*-
class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val):
		super(TreeNode, self).__init__()
		self.val = val
		self.left = None
		self.right = None

class Solution(object):
	"""docstring for Solution"""
	def __init__(self):
		super(Solution, self).__init__()
	
	def isValidBST(self,root):
		
		def helper(node,lower = float('-inf'),upper = float('inf')):
			if not node:
				return True
			if node.val <= lower or node.val>= upper:
				return False
			if not helper(node.left,lower,node.val):
				return False
			if not helper(node.right,node.val,upper):
				return False
			return True
		return helper(root)

	def numsOfValidBST(self,n):
		#G(n)==> 长度为n的序列的BST个数
		#F(i,n)==> 以i为根的不同BST的个数
		#G(n) ==> sum(F(i,n) for i in range(1,n+1))
		G = [0]*(n+1)
		G[0] = 1
		G[1] = 1 
		for i in xrange(2,n+1):
			for j in xrange(1,i+1):
				G[i] += G[j-1]*G[i-j]
		return G[n]

if __name__ == '__main__':
	s = Solution()
	root = TreeNode(5)
	root.left = TreeNode(1)
	root.right= TreeNode(4)
	root.right.left = TreeNode(3)
	root.right.right = TreeNode(6)
	print 'AA' ,s.numsOfValidBST(3)
	


					