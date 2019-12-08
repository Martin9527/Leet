# -*- coding: UTF-8 -*-
class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self,key = None,value = None):
		super(ListNode, self).__init__()
		self.key = key
		self.value = value
		self.pre = None
		self.next = None
		
class LRUCache(object):

	def __init__(self,capacity):
		self.capacity = capacity
		self.hashMap = {}
		self.head = ListNode()
		self.tail = ListNode()
		self.head.next = self.tail
		self.tail.pre = self.head

	def put(self,key,value):
		if key not in self.hashMap:
			if len(self.hashMap) >= self.capacity:
				self.removeNodeFromTail()
			node = ListNode(key,value)
			self.hashMap[key] = node
			self.moveNodeToHead(node)
			
		else:
			node = self.hashMap[key]
			node.pre.next = node.next
			node.next.pre = node.pre
			self.moveNodeToHead(node)


	def get(self,key):
		if key not in self.hashMap:
			return -1
		else:
			node = self.hashMap[key]
			node.pre.next = node.next
			node.next.pre = node.pre
			self.moveNodeToHead(node)
			return node.value

	def moveNodeToHead(self,node):
		node.next = self.head.next
		node.next.pre = node
		self.head.next = node
		node.pre = self.head

	def removeNodeFromTail(self):
		node = self.tail.pre
		node.pre.next = self.tail
		self.tail.pre = node.pre
		del self.hashMap[node.key]

if __name__ == '__main__':
	cache = LRUCache(2)
	cache.put(1, 1);
	cache.put(2, 2);
	print cache.get(1);       # 返回  1
	cache.put(3, 3);    # 该操作会使得密钥 2 作废
	print cache.get(2);       # 返回 -1 (未找到)
	cache.put(4, 4);    # 该操作会使得密钥 1 作废
	print cache.get(1);       # 返回 -1 (未找到)
	print cache.get(3);       # 返回  3
	print cache.get(4);       # 返回  4
