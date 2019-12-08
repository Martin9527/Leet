class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None
class Solution(object):
	def reverseKGroup(self,head,k):
		dummy = ListNode(0)
		dummy.next = head
		pre = dummy
		end = dummy
		while end.next:
			i = 0
			while i < k and end:
				end = end.next
				i += 1
			if end is None:
				break
			start = pre.next
			next = end.next
			end.next = None
			pre.next = self.reverse(start)
			start.next = next
			pre = start
			end = pre
		return dummy.next


	def reverse(self,head):
		pre = None
		cur = head
		while cur:
			next = cur.next
			cur.next = pre
			pre = cur
			cur = next
		return pre
			


	
if __name__ == '__main__':
	s = Solution()