class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		left = ["(","{","["]
		right = [")","}","]"]
		pair = {")":"(","}":"{","]":"["}
		stack = []
		if s == "":
			return True
		for c in s:
			if c in left:
				stack.append(c)
			elif c in right:
				if stack == []:
					return False
				if pair[c] != stack.pop():
					return False
		if stack == []:
			return True
		return False
				
