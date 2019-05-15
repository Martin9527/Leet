class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		#把一个zigzag看成一个v字
		#每一个v字看成一组zigzag
		#则每个v字的size = 2*numRows - 2
		#垂直列的字符之间相差 size
		#斜着的字符在本组内的位置为size - i,当前组的个数为j -i,即斜着的字符位置为：(j-i) + (size-i)
		if s is None or numRows <= 0 or s == '':
			return ''
		strLen = len(s)
		if strLen == 1 or strLen <= numRows or numRows == 1:
			return s
		target = []
		step = (2 * numRows) - 2
		for i in range(numRows):
			for j in range(i,strLen,step):
				target.append(s[j])
				if(i!= 0 and i!= numRows - 1 and (j-i) + (step-i) < strLen):
					target.append(s[(j-i) + (step-i)])
				else:
					pass
		ss = ''.join(target)

		return ss
if __name__ == '__main__':
	s = Solution()
	ss = s.convert('PAYPALISHIRING',3)



