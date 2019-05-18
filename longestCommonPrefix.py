class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		if len(strs) <= 0:
			return ''
		shortest = min(strs,key=len)
		print 'shortest: ',shortest
		for i,char in enumerate(shortest):
			for string in strs:
				if string[i] != char:
					return shortest[:i]
		return shortest
	

		
if __name__ == '__main__':
	so = Solution()
	s = ["dog","racecar","car"]
	ss = so.longestCommonPrefix(s)
	print 'AA: ',ss
