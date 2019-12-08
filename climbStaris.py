class Solution(object):
	"""docstring for Solution"""
	def climbStairs(self,n):
		if n > 2:
			#choose 1 first:
			return self.climbStairs(n-1) + self.climbStairs(n-2)
		elif n == 2:
			return 2
		else:
			return 1

	def climbStairs2(self,n):
		if n == 1:
			return
		dp = [0]*(n+1)
		dp[1] = 1
		dp[2] = 2
		for i in xrange(3,n+1):
			dp[i] = dp[i-1] + dp[i-2]

		return dp[n]


if __name__ == '__main__':
	s = Solution()
	print 'sss: ',s.climbStairs2(35)		