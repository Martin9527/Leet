class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None
class Solution(object):
	#Brute-force search
	def removeNthFromEnd1(self, head, n):
		"""
		:type head: ListNode 
		:type n: int
		:rtype: ListNode
		"""
		count = 0 
		t = head
		if t == None or t.next == None and n >= 1:
			return None
		while t!= None:
			count += 1
			t = t.next

		print 'count: ',count
		target = count - n
		if target == 0 :
			temp = head
			head = temp.next
			print 'del: ',temp.val
			del temp
		else:
			temp = head
			i = 1
			while i <= target:
				before = temp
				temp = temp.next
				i += 1
			before.next = temp.next
			print 'del: ',temp.val
			del temp
		return head

	def removeNthFromEnd(self,head,n):
		t = head
		if t == None or t.next == None and n >= 1:
			return None
		i = 1
		beforeNode = None
		while i < n + 1:
			beforeNode  = t
			t = t.next
			i += 1
		#beforeNode.next = t
		t = ListNode(0)
		t.next = head
		headChanged =True
		while beforeNode.next != None:
			t = t.next
			beforeNode = beforeNode.next
			headChanged = False
		if not headChanged:
			temp = t.next
			t.next =temp.next
			print 'del: ',temp.val
			del temp
			return head
		else:
			temp = t.next
			head =temp.next
			print 'del: ',temp.val
			del temp
		return head




		




				

		

if __name__ == '__main__':
	s = Solution()
	head = ListNode(1)
	ss = ListNode(2)
	head.next = ss
	s.removeNthFromEnd(head,2)
	print 'head: ',head.val

