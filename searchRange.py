# -*- coding: UTF-8 -*-
class Solution(object):
	
	def searchRange(self,nums,target):
		if not nums or target not in nums:
			return [-1,-1]
		res = []
		res.append(self.left_bound(nums,target))
		res.append(self.right_bound(nums,target))
		return res
		
	def binarySearch(self,nums,target):
		left = 0
		right = len(nums) - 1
		targetIndx = -1
		while left <= right:
			mid = (right + left) / 2
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				left = mid + 1
			elif nums[mid] > target:
				right = mid - 1
		
		return targetIndx

	def left_bound(self,nums,target):
		if not nums:
			return -1
		left = 0
		right = len(nums)
		while left < right:
			mid = (right + left) / 2
			if nums[mid] == target or nums[mid] > target:
				right = mid
			elif nums[mid] < target:
				left = mid + 1
		if nums[left] == target:
			return left
		else:
			return -1

	def right_bound(self,nums,target):
		if not nums:
			return -1
		left = 0
		right = len(nums)
		while left < right:
			mid = (right + left) / 2
			if nums[mid] == target or nums[mid] < target:
				left = mid + 1
			elif nums[mid] > target:
				right = mid

		if nums[left - 1] == target:
			return left - 1
		else:
			return -1
			
	




if __name__ == '__main__':
	s = Solution()
	nums = [1,2,3,3,3,3,4,6,8,9,12]
	nums2 = [1,2,2]
	print 'curAns: ',s.binarySearch(nums,3)
	print 'bounds: ',s.searchRange(nums,3)
