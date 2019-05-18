class Solution(object):	

	def romanToInt(self,s):
		'''
		
		'''
		length = len(s)
		if length <= 0:
			return 0
		num = 0
		i = 0
		while i < length:
			if s[i] == 'M':
				num += 1000
			elif s[i] == 'D':
				num += 500
			elif s[i] == 'C':
				if i + 1 < length:
					if s[i+1] == 'D':
						num += 400
						i += 2
						continue
					elif s[i+1] == 'M':
						num += 900
						i += 2
						continue
				num += 100
			elif s[i] == 'L':
				num += 50
			elif s[i] == 'X':
				if i + 1 < length:
					if s[i+1] == 'L':
						num += 40
						i +=2
						continue
					elif s[i+1] == 'C':
						num += 90
						i += 2
						continue
				num += 10
			elif s[i] == 'V':
				num += 5
			elif s[i] == 'I':
				if i + 1 < length:
					if s[i+1] == 'V':
						num += 4
						i += 2
						continue
					elif s[i+1] == 'X':
						num += 9
						i += 2
						continue
				num += 1
			else:
				raise
			i+= 1
		return num


if __name__ == '__main__':
	s = Solution()
	rom = s.romanToInt("MCMXCIV")
	print 'int: ',rom
	