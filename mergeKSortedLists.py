class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None
class Solution(object):
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
	def mergeKLists1(self,lists):
		result = None
		for l in lists:
			if result is None :
				result = l
			else:
				result = self.mergeTwoLists(result,l)
		return result

	def mergeKLists2(self,lists):
		vals = []
		for l in lists:
			while l:
				vals.append(l.val)
				l = l.next
		head = last = None
		for val in sort(vals):
			temp = ListNode(val)
			if not last:
				last = temp
			else:
				last.next = temp
				last =temp
			if not head:
				head = temp
		return head

	def mergeKLists3(self,lists):
		k = len(lists)
		if not k:
			return
		l = [l[0],for l in lists]
		minHeap = heapq.heapify(l)
		item = minHeap.pop()
		head = None
		last = None
		while item:
			node = ListNode(item.val)
			if not head:
				head = node
			if not last:
				last = node
			else:
				last.next = node
				last = node
			if item.next:
				minHeap.push(item.next)
			item = minHeap.pop()
		return head

			


	
if __name__ == '__main__':
	s = Solution()
