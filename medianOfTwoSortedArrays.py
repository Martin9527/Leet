class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		ls1 = len(nums1)
		ls2 = len(nums2)
		newLen =  ls1 + ls2
		newList = []
		idx1 = 0
		idx2 = 0
		if ls1 == 0:
			newList = nums2
		elif ls2 == 0 :
			newList = nums1
		else:
			for i in range(newLen):
				if nums1[idx1] > nums2[idx2]:
					newList.append(nums2[idx2])
					idx2 += 1
				else:
					newList.append(nums1[idx1])
					idx1 += 1
				if idx1 > (ls1 - 1):
					newList = newList + nums2[idx2:]
					break
				elif idx2 > (ls2 - 1):
					newList = newList + nums1[idx1:]
					break
				

		index = (newLen - 1 ) // 2
		if newLen % 2 == 1:
			median = newList[index]
		else:
			median = (newList[index] + newList[index + 1]) / 2.0
	
		return median

	def findKthInTwoSortedArray(self,nums1,nums2,k):
		l1 = len(nums1)
		l2 = len(nums2)
		if l1 + l2 < k:
			return 0
		if l1 == 0:
			return nums2[k-1]
		if k == 1:
			return nums1[0] if nums1[0] < nums2[0] else nums2[0]
		if l1 > l2:
			return self.findKthInTwoSortedArray(nums2,nums1,k)
		i = k/2 if l1 > k/2 else l1
		j = k/2 if l2 > k/2 else l2
		if nums1[i-1] < nums2[j-1]:
			return self.findKthInTwoSortedArray(nums1[i::],nums2,k-i)
		elif nums1[i-1] > nums2[j-1]:
			return self.findKthInTwoSortedArray(nums1,nums2[j::],k-j)
		else:
			return nums2[j-1]


	

if __name__ == '__main__':
	s = Solution()
	print s.findKthInTwoSortedArray([1,2,3],[5,6],6)