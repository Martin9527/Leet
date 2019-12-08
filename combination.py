# -*- coding: UTF-8 -*-
class Solution(object):
	
	def combinationSum(self, candidates, target):
		size = len(candidates)
		if size < 1:
			return []
		res = []
		def backTrack(candidates,begin,target,curAns):
			if target < 0:
				return
			if target == 0:
				res.append(curAns[:])
				return
			for i in xrange(begin,size):
				curAns.append(candidates[i])
				backTrack(candidates,i,target-candidates[i],curAns)
				curAns.pop()

		backTrack(candidates,0,target,[])
		print 'length: ',len(res)
		return res

	def combinationSum2(self,candidates,target):
		size = len(candidates)
		if size < 1:
			return []
		res = []
		def backTrack(candidates,begin,target,curAns):
			hashMap = set()
			if target < 0:
				return 
			if target == 0:
				res.append(curAns[:])
				return
			for i in xrange(begin,size):
				if candidates[i] in hashMap:
					continue
				else:
					hashMap.add(candidates[i])
					curAns.append(candidates[i])
					backTrack(candidates,i+1,target-candidates[i],curAns)
					curAns.pop()
		candidates.sort()
		backTrack(candidates,0,target,[])
		print 'length: ',len(res)
		return res




if __name__ == '__main__':
	s = Solution()
	nums = [10,1,2,7,6,1,5]
	print 'curAns: ',s.combinationSum2(nums,8)