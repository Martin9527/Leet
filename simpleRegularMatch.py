class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		if not p:
			return not s
		if p == '':
			return s == ''
		if s == '':
			return self.isEndOfStar(p)

		firstMatch = (s[0] == p[0] or p[0] == '.')
		if len(p) >= 2 and p[1]== '*':
			return self.isMatch(s,p[2:]) or (firstMatch and self.isMatch(s[1:],p))
		else:
			return firstMatch and self.isMatch(s[1:],p[1:])

	def isEndOfStar(self,p):
		while p != '':
			if len(p) == 1 or len(p) > 1 and p[1] != '*':
				return False
			p = p[2:]
		return True
	

		
if __name__ == '__main__':
	so = Solution()
	s = 'aa'
	p = 'a'
	ss = so.isMatch(s,p)
	print 'isMatch: ',ss



