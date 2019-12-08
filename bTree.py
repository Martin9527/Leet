#Defination of B-Tree and B+Tree
# Properties of B-Tree
# 1) All leaves are at same level.
# 2) A B-Tree is defined by the term minimum degree ‘t’. The value of t depends upon disk block size.
# 3) Every node except root must contain at least t-1 keys. Root may contain minimum 1 key.
# 4) All nodes (including root) may contain at most 2t – 1 keys.
# 5) Number of children of a node is equal to the number of keys in it plus 1.
# 6) All keys of a node are sorted in increasing order. The child between two keys k1 and k2 contains all keys in the range from k1 and k2.
# 7) B-Tree grows and shrinks from the root which is unlike Binary Search Tree. Binary Search Trees grow downward and also shrink from downward.
# 8) Like other balanced Binary Search Trees, time complexity to search, insert and delete is O(Logn).

class BTreeNode(object):
	"""docstring for BTreeNode"""
	def __init__(self, t,isleaf):
		super(BTreeNode, self).__init__()
		self.degree = t
		self.isLeaf = isleaf
		self.childNodes = [] #childNodes[i].key < key[i],childNodes[i+1].key > key[i]
		self.keys = []
		self.maxKeyNum = self.degree*2 - 1
		self.maxChildNum = self.degree * 2
		self.curChildNum = 0
		self.curKeyNum = 0
		self.data = [] #data stored in this node

	def traverse(self):
		pass

	def search(self,k):
		i = 0
		while i < self.curKeyNum and k > self.keys[i]:
			i += 1
		if keys[i] == k:
			return self
		if self.isLeaf:
			return None
		return self.childNodes[i].search(k)

	def insert(self,k):
		# 1) Initialize x as root.
		# 2) While x is not leaf, do following
		# 	..a) Find the child of x that is going to be traversed next. Let the child be y.
		# 	..b) If y is not full, change x to point to y.
		# 	..c) If y is full, split it and change x to point to one of the two parts of y. 
		# 			If k is smaller than mid key in y, then set x as the first part of y.
		# 			Else second part of y. When we split y, we move a key from y to its parent x.
		# 3) The loop in step 2 stops when x is leaf. x must have space for 1 extra key 
		# 	as we have been splitting all nodes in advance. So simply insert k to x.
		#not full,insert the key directly
		if self.curKeyNum < self.maxKeyNum: 
			self.directInsert(k)
		else:
			self.splitInsert(k)

	def directInsert(self,k):
		i = self.curKeyNum - 1
		while i >= 0 and self.keys[i] > k:
			i += 1
		self.keys[i] = k
		self.curKeyNum += 1

	def splitInsert(self,k):
		

	def delete(self,k):
		pass

	def splitChild(self,childIndex):
		pass

	def insertDirectly(self,k):


class BTree(object):
	"""docstring for BTree"""
	def __init__(self, root,t):
		super(BTree, self).__init__()
		self.root = root
		self.t = t

	def traverse(self):
		if self.root:
			root.traverse()

	def search(self,key):
		if self.root:
			self.root.search(key)

	def insert(self,key):
		pass

	def delete(self,key):
		pass

		
		