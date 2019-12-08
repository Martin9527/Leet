class Solution(object):
	def lengthOfLongestSubstring1(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		max_length = 0
		cur_length = 0
		subString =  []
		repeated = False
		i = 0
		usedChar = set()
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

	def lengthOfLongestSubstring2(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		max_length = 0
		cur_length = 0
		subString =  []
		repeated = False
		i = 0
		usedChar = set()
		n = len(s)
		if n == 0 or n == 1:
			return n
		i = j = 0
		while i < n and j < n:
			if s[j] not in usedChar:
				usedChar.add(s[j])
				max_length = max(max_length,j-i+1)
				j += 1
			else:
				usedChar.remove(s[i])
				i += 1
		return max_length
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0
		n = len(s)
		ans = set()
		left = 0
		max_length = 0
		cur_length = 0
		for i in range(n):
			cur_length += 1

			while s[i] in ans:
				ans.remove(s[left])
				left += 1
				cur_length -= 1
				
			if cur_length > max_length:
				max_length = cur_length
			ans.add(s[i])

				
		print "ans",ans
		return max_length


        
if __name__ == '__main__':
	s = Solution()
	print 'length: ',s.lengthOfLongestSubstring2("abcabababa")
	