#--utf-8 -#
class Heap(object):
	def __init__(self, k):
		super(Heap, self).__init__()
		self._capactiy = k
		self._data = []
		self._count = 0

	def add(self,item):
		self._data.append(item)
		self._count += 1
		self._shiftUp(self._count - 1)

	def pop(self):
		item = self._data[0]
		self._data[0] = self._data[self._count - 1]
		self._count -= 1
		self._shiftDown(0)
		return item

	def top(self,k = 0):
		if k:
			return self._data[0:k]
		else:
			return self._data[0]

	def all(self):
		return self._data[:self._count]

class MaxHeap(Heap):
	
	def _shiftUp(self,index):
		#pop up: compare with parent
		child = index
		parent = 1
		while parent > 0 :
			parent = (child - 1) / 2
			if self._data[parent] < self._data[child]:
				self._data[parent],self._data[child] = self._data[child],self._data[parent]
				child = parent
			else:
				break


	def _shiftDown(self,index):
		#drop down: compare with children
		parent = index
		child = 0
		child = 2*parent + 1
		while child < self._count - 1:
			if self._data[parent] < self._data[child]:
				self._data[parent],self._data[child] = self._data[child],self._data[parent]
				parent = child
				child = 2*parent + 1

			else:
				break

class MinHeap(Heap):
	
	def _shiftUp(self,index):
		#pop up: compare with parent
		child = index
		parent = 1
		while parent > 0 :
			parent = (child - 1) / 2
			if self._data[parent] > self._data[child]:
				self._data[parent],self._data[child] = self._data[child],self._data[parent]
				child = parent
			else:
				break


	def _shiftDown(self,index):
		#drop down: compare with children
		parent = index
		child = 0
		child = 2*parent + 1
		while child < self._count - 1:
			if self._data[parent] > self._data[child]:
				self._data[parent],self._data[child] = self._data[child],self._data[parent]
				parent = child
				child = 2*parent + 1

			else:
				break


if __name__ == '__main__':
	minHeap = MinHeap(10)
	map(minHeap.add,[1,3,5,7,9,2,4,6,8,0])
	#print 'AAA: ',minHeap.top(5)
	print 'pop: ',minHeap.pop()
	#print 'BBB: ',minHeap.top(5)
	print 'ALL: ',minHeap.all()
	a = [1,3,5,7,9,2,4,6,8,0]
	 import heapq
	heapq.heapify(a)
	heapq.heappop(a)
	print 'dddd: ',a


