#--utf-8 -#
# Definition for singly-linked list.

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers1(self, l1, l2):
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

	def addTwoNumbers(self,l1,l2):
		p = l1
		q = l2
		firstNode = ListNode(0)
		curNode = firstNode
		carry = 0
		while p or q:
			pVal = p.val if p else 0
			qVal = q.val if q else 0
			sumVal = pVal + qVal + carry
			carry = sumVal / 10
			dump = ListNode(sumVal % 10)
			curNode.next = dump
			curNode = dump
			if p:
				p = p.next
			if q:
				q = q.next
		if carry:
			curNode.next = ListNode(carry)
		return firstNode.next

	def addTwoNumbers2(self,l1,l2):
		# list is Big order 
		s1 = []
		s2 = []
		p = l1
		q = l2

		while p :
			s1.append(p.val)
			p = p.next
		while q:
			s2.append(q.val)
			q = q.next

		carry = 0
		curNode = None

		while s1 and s2:
			val1 = s1.pop()
			val2 = s2.pop()
			sumVal = carry + val1 + val2
			carry = sumVal / 10
			dumpNode = ListNode(sumVal % 10)
			dumpNode.next = curNode
			curNode = dumpNode
		while s1:
			val1 = s1.pop()
			sumVal = carry + val1
			carry = sumVal / 10
			dumpNode = ListNode(sumVal % 10)
			dumpNode.next = curNode
			curNode = dumpNode
		while s2:
			val2 = s2.pop()
			sumVal = carry + val2
			carry = sumVal / 10
			dumpNode = ListNode(sumVal % 10)
			dumpNode.next = curNode
			curNode = dumpNode
		if carry:
			dumpNode = ListNode(carry)
			dumpNode.next = curNode
			curNode = dumpNode
		return curNode

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
	l1 = s.createListNode([6,4,3])
	l2 = s.createListNode([5,7,2])
	r = s.addTwoNumbers2(l1,l2)
	print 'rrr: ',r.val,r.next.val,r.next.next.val,r.next.next.next.val



        