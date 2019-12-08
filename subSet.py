# -*- coding: UTF-8 -*-
class Solution(object):
	
	def subsets(self,nums):
		size = len(nums)
		if size < 1:
			return []
		res = []
		def backTrack(i,tmp):
			res.append(tmp)
			for j in xrange(i,size):
				backTrack(j+1,tmp+[nums[j]])
		backTrack(0,[])
		return res

	def subsets2(self,nums):
		#with dumplicate element in nums
		size = len(nums)
		if size < 1:
			return []
		res = []
		def backTrack(i,tmp):
			res.append(tmp)
			for j in xrange(i,size):
				if j > i and nums[j] == nums[j-1]:
					continue

				backTrack(j+1,tmp+[nums[j]])
		nums.sort()
		backTrack(0,[])
		return res




if __name__ == '__main__':
	s = Solution()
	nums = [1,2,3]
	nums2 = [1,2,2]
	print 'curAns: ',s.subsets(nums)
	print 'curAns2: ',s.subsets2(nums2)