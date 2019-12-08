class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy 
        while tmp.next and tmp.next.next:
           start = tmp.next
           end = tmp.next.next
           tmp.next = end
           start.next = end.next
           end.next = start
           tmp = start
        return dummy.next
if __name__ == '__main__':
  s = Solution()