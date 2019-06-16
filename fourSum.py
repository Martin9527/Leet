class Solution(object):
	#Brute-force search
	def fourSum1(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		nums.sort()
		ls = len(nums)
		result = []
		if ls < 4:
			return []
		for i in range(ls):
			for j in range(i+1,ls):
				for k in range(j+1,ls):
					for l in range(k+1,ls):
						if nums[i] + nums[j] + nums[k] + nums[l] == target:
							t = [nums[i],nums[j],nums[k],nums[l]]
							if t not in result:
								result.append(t)
		return result
	#like three-sum
	def fourSum(self,nums,target):
		nums.sort()
		ls = len(nums)
		result = []
		if ls < 4:
			return []
		index_pair = {}
		combos = {}
		for i in range(ls):
			for j in range(i+1,ls):
				half_sum = nums[i] + nums[j]
				if index_pair.get(target - half_sum) is not None:
					pairs = index_pair[target-half_sum]
					for pair in pairs:
						if i !=pair[0] and i!= pair[1] and j != pair[0] and j!= pair[1]:
							combo = sorted((nums[i], nums[j], nums[pair[0]], nums[pair[1]])) 
							combos[tuple(combo)] = True
				if index_pair.get(half_sum) is not None:
					index_pair[half_sum].append((i,j))
				else:
					index_pair[half_sum] = [(i,j)]
				
		return combos.keys()
	#general k sum problem solution
	def kSum(self,nums,target,k,currentResult,finalResults):
		'''
			currentResult: it reprensent middle result
			finalResults: it is the final results
		'''
		ls = len(nums)
		if ls < k:
			return []
		#it is two Sum problem
		if k == 2:
			begin, end = 0, len(nums) - 1
			while begin < end:
				curr = nums[begin] + nums[end]

				if curr == target:
					results.append(result + [nums[i], nums[j]])
					begin +=1
					end -= 1
					while begin < end and nums[begin] == nums[begin-1]:
						begin +=1
					while begin < end and nums[end] == nums[end+1]:
						end -=1
						pass
				elif curr < target:
					begin += 1
				else:
					end -= 1
		#reduce to two Sum problem
		else:
			for i in range(ls-k+1):
				if i > 0 and nums[i] == nums[i-1]:
					continue
				n = nums[i]
				self.kSum(nums[i+1:],target-n,k-1,currentResult+[n],finalResults)
				

				

		

if __name__ == '__main__':
	s = Solution()
	nums = [-479,-472,-469,-461,-456,-420,-412,-403,-391,-377,
	-362,-361,-340,-336,-336,-323,-315,-301,-288,-272,-271,-246,
	-244,-227,-226,-225,-210,-194,-190,-187,-183,-176,-167,-143,
	-140,-123,-120,-74,-60,-40,-39,-37,-34,-33,-29,-26,-23,-18,
	-17,-11,-9,6,8,20,29,35,45,48,58,65,122,124,127,129,145,164,
	182,198,199,206,207,217,218,226,267,274,278,278,309,322,323,
	327,350,361,372,376,387,391,434,449,457,465,488]
	target = 1979
	result = []
	s.kSum(nums,target,4,[],result)
	print result
