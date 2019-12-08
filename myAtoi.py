INT_MIN = -0x80000000
INT_MAX = 0x7fffffff
class Solution(object):
	def myAtoi(self, targetStr):
		"""
		:type str: str
		:rtype: int
		"""
		numbers = ['0','1','2','3','4','5','6','7','8','9']
		signs = ['+','-']

		if targetStr is None:
			return 0
		i = 0
		targetStr = targetStr.strip()
		if targetStr == '':
			return 0
		length = len(targetStr)
		print targetStr
		if targetStr[0] not in signs and targetStr[0] not in numbers:
			return 0
		idx = endIdx = 0
		for i in range(1,length):
			if targetStr[i] not in numbers:
				endIdx = i - 1
				break
			endIdx = i
		if endIdx == 0 and targetStr[0] not in numbers:
			return 0
		if targetStr[0] == '+':
			indics = 1
		elif targetStr[0] == '-':
			indics = -1
		else:
			indics = 0
		idx = 1 if indics else 0
		ss = targetStr[idx:endIdx + 1]
		nn = int(ss)
		if indics:
			nn *= indics
		if nn > INT_MAX:
			return INT_MAX
		elif nn < INT_MIN:
			return INT_MIN
		else:
			return nn
	
	def myAtoi2(self,targetStr):
		import re
		return max(min(int(*re.findall('^[\+\-]?\d+',targetStr.strip())),INT_MAX),INT_MIN)
		
		



if __name__ == '__main__':
	s = Solution()
	nn = s.myAtoi2("   +0 123")
	print 'nn: ',nn
	
	