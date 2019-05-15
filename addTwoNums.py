# Definition for singly-linked list.

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""

		node = l1
		value1 = 0
		value2 = 0
		i = j = 0
		while node.next:
			value1 += node.val * (10**i)
			node = node.next
			i += 1
		value1 += node.val * (10**i)
		node = l2
		while node.next:
			value2 += node.val * (10**j)
			
			node = node.next
			j += 1
		value2 += node.val * (10**j)
		sum_value = int(value1 + value2)
		str_value = str(sum_value)[::-1]
		
		firstNode = lastNode = None
		for i, ch in enumerate(str_value):
			node = ListNode(int(ch))
			if firstNode is None:
				firstNode = node
			if lastNode is None:
				lastNode = node
			else:
				lastNode.next = node
				lastNode = node
			
		return firstNode

	def createListNode(self,nums):
		firstNode = lastNode = None
		for i, ch in enumerate(nums):
			
			node = ListNode(ch)
			if firstNode is None:
				firstNode = node
			
			if lastNode is None:
				lastNode = node
			else:
				lastNode.next = node
				lastNode = node
				
		return firstNode


if __name__ == '__main__':
	s = Solution()
	l1 = s.createListNode([2,4,3])
	l2 = s.createListNode([5,6,4])
	s.addTwoNumbers(l1,l2)



        