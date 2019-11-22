class Solution(object):
	def maxArea3(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		if not height or len(height) < 2:
			return 0
		maxArea = 0
		for i in range(len(height)):
			for j in range(i,len(height)):
				h = min(height[i],height[j])
				maxArea = max(maxArea,(j-i)*h)
		return maxArea

	def maxArea2(self,height):
		if not height or len(height) < 2:
			return 0
		maxArea = 0
		length = len(height)
		i = 0
		j = length - 1
		while i < length and j >= i:
			h = min(height[i],height[j])
			maxArea = max(maxArea,(j - i)*h)
			if height[i] < height[j]:
				i += 1
			else:
				j -= 1
		return maxArea

		

if __name__ == '__main__':
	so = Solution()
	maxArea = so.maxArea3([1,8,6,2,5,4,8,3,7])
	print 'AAA: ',maxArea
	
	


