class Solution(object):

	def threeSumClosest(self,nums,target):
	
		length = len(nums)
		if length < 3:
			return 0
		nums.sort()
		result = nums[0] + nums[1] + nums[2]
		min_target = (result - target)
		for i in xrange(length-2):
			j = i + 1
			k = length - 1
			while j < k:
				cur = nums[i] + nums[j] + nums[k]
				last = abs(cur - target)
				if cur == target:
					return target
				else:
					if last < abs(result - target):
						result = cur
					if cur < target:
						j += 1
					else:
						k -= 1
		return result


			

		
if __name__ == '__main__':
	so = Solution()
	nums = [-1, 2, 1, -4]
	res = so.threeSumClosest(nums,1)
	print 'result: ',res

