class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		max_length = 0
		cur_length = 0
		subString =  []
		repeated = False
		i = 0
		if len(s) == 0 or len(s) == 1:
			return len(s)
		while i < len(s):
			if s[i] not in subString:
				subString.append(s[i])
				if len(subString) > max_length:
					max_length = len(subString)
			else:
				oldIdx = 0
				for Idx,char in enumerate(subString):
					if char == s[i]:
						oldIdx = Idx
						break
				if oldIdx == (i - 1):
					del subString[:]
					subString.append(s[i])
				else:
					subString = subString[oldIdx + 1:]
					subString.append(s[i])
			i += 1
	
		return max_length

        
if __name__ == '__main__':
	s = Solution()
	print 'length: ',s.lengthOfLongestSubstring("pwwkew")
	