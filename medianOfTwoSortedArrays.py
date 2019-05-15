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


	

if __name__ == '__main__':
	s = Solution()
	s.findMedianSortedArrays([],[1])