class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None
class Solution(object):
	def mergeTwoLists2(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if l1 is None:
			return l2
		if l2 is None:
			return l1
		p1 = l1
		p2 = l2
		head = ListNode(0)
		current = None
		while p1!= None and p2!= None:
			if p1.val < p2.val:
				if current:
					current.next = p1
				current = p1
				p1 = p1.next
			else:
				if current:
					current.next = p2
				current = p2
				p2 = p2.next
			current.next = None
			if head.next is None:
				head.next = current
		if p1 == None:
			current.next = p2
		else:
			current.next = p1
		return head.next
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if l1 is None:
			return l2
		if l2 is None:
			return l1
		while l1 and l2:
			if l1.val < l2.val:
				l1.next = self.mergeTwoLists(l1.next,l2)
				return l1
			else:
				l2.next = self.mergeTwoLists(l1,l2.next)
				return l2
if __name__ == '__main__':
	s= Solution()
	l1 = ListNode(1)
	l1.next = ListNode(2)
	l1.next.next = ListNode(4)
	l2 = ListNode(1)
	l2.next = ListNode(3)
	l2.next.next = ListNode(4)
	l = s.mergeTwoLists(l1,l2)
	while l!=None:
		print 'l.val: ',l.val
		l = l.next