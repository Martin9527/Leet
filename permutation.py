class Solution(object):
	def permute(self,nums):
		size = len(nums)
		if not size :
			return []
		result = []
		curAns = []
		usedNums = set()
		self.backTrack(nums,size,curAns,usedNums,result)
		return result

	def backTrack(self,nums,size,curAns,usedNums,result):
		if size == len(curAns):
			import copy
			ans = copy.deepcopy(curAns)
			result.append(ans)
			return
		for j in range(size):
			if nums[j] not in usedNums:
				usedNums.add(nums[j])
				curAns.append(nums[j])
				self.backTrack(nums,size,curAns,usedNums,result)
				usedNums.remove(nums[j])
				curAns.pop()
	def permuteUnique(self,nums):
		size = len(nums)
		if size < 1:
			return []
		res = []
		usedNums = set()
		def backTrack(nums,begin,curAns,usedNums):
			if len(curAns) == size:
				res.append(curAns[:])
				return
			hashMap = set()
			for j in xrange(size):
				if nums[j] in hashMap:
					continue
				else:
					hashMap.add(nums[j])
					if nums[j] not in usedNums:
						usedNums.add(nums[j])
						curAns.append(nums[j])
						self.backTrack(nums,size,curAns,usedNums)
						usedNums.remove(nums[j])
						curAns.pop()
		nums.sort()
		backTrack(nums,0,[],usedNums)
		print 'length: ',len(res)
		return res

if __name__ == '__main__':
	s = Solution()
	nums = [1,1,2]
	ans = s.permute(nums)
	print 'AA: ',len(ans),ans