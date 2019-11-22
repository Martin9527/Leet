class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		totalWater = 0
		if not height or len(height) < 1:
			return totalWater
		for i in xrange(1,len(height) - 1):
			j = i - 1
			maxLeft = 0
			while j >= 0:
				maxLeft = max(maxLeft,height[j])
				j -= 1
			maxRight = 0
			j = i + 1
			while j < len(height):
				maxRight = max(maxRight,height[j])
				j += 1
			minHeight = min(maxLeft,maxRight)
			if minHeight > height[i]:
				totalWater += minHeight - height[i]
		return totalWater

	def trap1(self,height):
		size = len(height)
		maxLeft,maxRight = [0]*size,[0]*size
		maxLeft[0] = height[0]
		maxRight[size -1] = height[size-1]
		for i in xrange(1,size - 1):
			maxLeft[i] = max(height[i],maxLeft[i-1])
		for i in reversed(xrange(1,size-1)):
			maxRight[i] = max(height[i],maxRight[i+1])
		totalWater = 0
		for i in xrange(1,size-1):
			minHeight = min(maxLeft[i],maxRight[i])
			if minHeight > height[i]:
				totalWater +=  minHeight - height[i]
		return totalWater


		

if __name__ == '__main__':
	so = Solution()
	maxArea = so.trap1([0,1,0,2,1,0,1,3,2,1,2,1])
	print 'AAA: ',maxArea