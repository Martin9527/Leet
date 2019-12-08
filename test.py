
def medianOfTwoSortedArrays(nums1,nums2):
	
	if len(nums1) > len(nums2):
		nums1,nums2 = nums2,nums1
	m = len(nums1)
	n = len(nums2)
	imin = 0
	imax = m
	half_len = (m+n+1) / 2
	print 'iii: ',nums1,nums2,imin,imax,m,n
	while imin <= imax:
		i = (imin + imax) / 2
		j = half_len - i
		print "i = {},j ={}".format(i,j)
		if i<m and nums1[i] < nums2[j-1]:
			imin = i + 1
		elif i>0 and nums2[j] < nums1[i-1]:
			imax = i -1
		else:
			if i == 0:
				max_left_part = nums2[j-1]
			elif j == 0:
				max_left_part = nums1[i-1]
			else:
				max_left_part = max(nums1[i-1],nums2[j-1])

			#find the median
			if(m+n) % 2 == 1:
				median = max_left_part
				print 'median: ',median
				return
			if i== m:
				min_right_part = nums2[j]
			elif j == n:
				min_right_part = nums1[i]
			else:
				min_right_part = min(nums1[i],nums2[j])

			median = (max_left_part+min_right_part) / 2.0
			print 'median: ',median
			return median

def longestPalindromaicString(s):
	if not s or len(s)<=1:
		return s
	size = len(s)
	#dp[l][r] = True means s[l:r+1] is palindromaicString
	dp = [[False]*size]*size
	dp1 = [[False for _ in range(size)] for _ in range(size)]

	print 'dp: ',dp
	print 'dp1: ',dp1
	maxLen = 1
	subString = s[0]
	for r in xrange(1,size):
		for l in xrange(r):
			if s[l] == s[r] and (len(s[l:r+1]) <= 3 or dp[l+1][r-1]):
				dp[l][r] = True
				if maxLen < len(s[l:r+1]):
					subString = s[l:r+1]
					maxLen = len(subString)
					print 'maxLen: ',maxLen,subString

	return maxLen
def zigZag(s,numRows):
	if not s or not numRows:
		return ''
	if numRows < 2:
		return s
	res = ['']*numRows
	rowIndex = 0
	flag = -1
	for c in s:
		res[rowIndex] += c
		if rowIndex == numRows -1 or rowIndex == 0:
			flag = -flag
		rowIndex += flag
	return ''.join(res)

def isMatch(s,p):
	if s == '':
		if p == '' or p == '.' or p == '.*':
			return True
		else:
			return False
	if '*' not in p and '.' not in p and p != s:
		return False
	matchedIdx = 0
	size = len(p)
	for idx,char in enumerate(s):
		print 'start: ',matchedIdx,char
		if matchedIdx >= size:
			return False
		if p[matchedIdx] == char:
			matchedIdx += 1
			print 'tttttttt'
			continue
		elif p[matchedIdx] == '.':
			matchedIdx += 1
			print 'ssssss'
			continue
		elif p[matchedIdx] == '*' and matchedIdx > 0 and p[matchedIdx -1] == char or p[matchedIdx-1] == '.':
			print 'ddddddd'
			continue
		elif matchedIdx + 1 < size and p[matchedIdx+1] == '*':
			#matchedIdx += 2
			if matchedIdx + 2 < size:
				p = p[matchedIdx+2:]
				
				return isMatch(s,p)
			else:
				return False
			print 'ffff'
			continue
		else:
			return False
	return True

def maxArea(height):
	size = len(height)
	maxArea = 0
	for i in xrange(size):
		for j in xrange(size):
			maxArea = max(maxArea,abs((j-i))*min(height[i],height[j]))
	return maxArea

def maxArea(height):
	size = len(height)
	i = 0
	j = size-1
	maxArea = 0
	
def twoSum(nums ,target):
	tmp = {}
	for i,num in enumerate(nums):
		if target - num not in tmp:
			tmp[num] = i
		else:
			return [i,tmp[targe-num]]

def threeSum1(nums,target):
	if not nums or len(nums) < 3:
		return []
	visited = {}
	nums.sort()
	result,visiited = [],{}
	size = len(nums)
	tmp = {}
	minTarget = 0
	for i in xrange(size-2):
		if nums[i] not in visiited:
			tmp,visiited[nums[i]] = {},True
			tmpTarget = target - nums[i]
			for j in xrange(i+1,size):
				if tmpTarget - nums[j] not in tmp:
					tmp[nums[j]] = j
				else:
					result.append([nums[i],tmpTarget-nums[j],nums[j]])

	return result

def threeSum(nums,target):
	if not nums or len(nums) < 3:
		return []
	res = []
	size = len(nums)
	nums.sort()
	for i in xrange(size):
		if nums[i] > target:
			return res
		if i > 0 and nums[i] == nums[i - 1]:
			continue
		l = i + 1
		r = size - 1
		while l <= r:
			tmpSum = nums[i] + nums[l] + nums[r]
			if tmpSum == target:
				res.append([nums[i],nums[l],nums[r]])
				while l < r and nums[l] == nums[l+1]:
					l += 1
				while l < r and nums[r] == nums[r-1]:
					r -= 1
				l += 1
				r -= 1
			elif tmpSum < target:
				l += 1
			else:
				r -= 1
	return res

def threeSumCloset(nums,target):
	if not nums or len(nums) < 3:
		return []
	nums.sort()
	size = len(nums)
	minRes = nums[0] + nums[1] + nums[2]
	for i in xrange(size-2):
		l = i+1
		r = size-1
		while l<r:
			curSum = nums[i]+nums[l]+nums[r]
			if curSum == target:
				return curSum
			if abs(curSum - target) < abs(minRes - target):
				minRes = curSum
			if curSum > target:
				r -= 1
			else:
				l += 1
	return minRes


		


if __name__ == '__main__':
	nums1 = [1, 2]
	nums2 = [3, 4]
	#medianOfTwoSortedArrays(nums1,nums2)
	height = [1,8,6,2,5,4,8,3,7]
	nums = [-1,2,1,-4]
	print 'tt: ',threeSumCloset(nums,1)
