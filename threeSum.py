class Solution(object):

	def threeSum(self, nums):
		result = []
		length = len(nums)
		if length < 3:
			return result
		nums.sort()
		for i in range(length-2):
			if i > 0 and nums[i] == nums[i-1]:
				continue
			j = i + 1
			k = length - 1
			while j < k:
				cur = nums[i] + nums[j] + nums[k]
				if cur == 0:
					result.append([nums[i],nums[j],nums[k]])
					while j < k and nums[j] == nums[j+1]:
						j += 1
					while j < k and nums[k] == nums[k-1]:
						k -= 1
					j += 1
					k -= 1
				elif cur < 0:
					j += 1
				else:
					k -= 1
		return result

	def threeSum2(self,nums):
		
		length = len(nums)
		if length < 3:
			return []
		nums.sort()
		visited = {}
		result = set()
		for i in xrange(length-2):
			table,target ={}, -nums[i]
			if nums[i] not in visited:
				for j in xrange(i+1,length):
					if nums[j] not in table:
						table[target - nums[j]] = j
					else:
						result.add((nums[i],target - nums[j],nums[j]))
				visited[nums[i]] = 1
		return list(result)


			

		
if __name__ == '__main__':
	so = Solution()
	nums = [-1,0,1,2,-1,-4]
	res = so.threeSum2(nums)
	print 'result: ',res

