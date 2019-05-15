# -*- coding: utf-8 -*-
class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		rs = s[::-1]
		ls = len(s)
		static = [[0] * ls for i in range(ls)]
		maxLength = 0
		index = 0
		subString = ''
		for i in range(ls):
			for j in range(ls):
				if s[i] == rs[j]:
					if i == 0 or j == 0:
						static[i][j] = 1
					else:
						static[i][j] = static[i-1][j-1] + 1
					
					if static[i][j] > maxLength:
						oldIndex = index
						oldMax = maxLength
						oldSub = subString
						index = i - static[i][j] + 1
						maxLength = static[i][j]
						subString = s[index:index + maxLength]
						if subString[0] != subString[-1]:
							maxLength = oldMax
							index = oldIndex
							subString = oldSub

		return subString



if __name__ == '__main__':
	s = Solution()
	s.longestPalindrome("aacdefcaa")