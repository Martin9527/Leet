# -*- coding: UTF-8 -*-
class Solution(object):
	def maxProfit1(self,prices):
		maxProfit = 0
		for i in xrange(len(prices)-1):
			for j in xrange(i+1,len(prices)):
				maxProfit = max(maxProfit,(prices[j] - prices[i]))
		maxProfit = max(0,maxProfit)
		return maxProfit

	def maxProfit2(self,prices):
		size = len(prices)
		if size < 2:
			return 0
		maxProfit = 0
		minVal = prices[0]
		for i in range(1,size):
			maxProfit = max(maxProfit,prices[i]-minVal)
			minVal = min(minVal,prices[i])
		return maxProfit

	def maxProfit(self,prices):
		size = len(prices)
		if size < 2:
			return 0
		dp = [[0,0] for i in range(size)]
		#dp[i][0]  代表第i天不持有股票的最大收益
		#dp[i][1] 代表第i天持有股票的最大收益
		dp[0][0] = 0
		dp[0][1] = -prices[0]
		for i in xrange(1,size):
			dp[i][0] = max(dp[i-1][0],dp[i-1][1] + prices[i])
			dp[i][1] = max(dp[i-1][1],-prices[i])

		return dp[size-1][0]


if __name__ == '__main__':
	s = Solution()
	prices = [7,6,4,3,15]
	print 'maxProfit: ',s.maxProfit(prices)