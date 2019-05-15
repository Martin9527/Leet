class Solution(object):
	def intToRoman(self,num):
		'''
		
		'''
		roman = []
		while num > 0:
			if num >= 1000:
				m = num // 1000
				num = num % 1000
				roman.append("M"*m)
			elif num >= 900:
				num = num - 900
				roman.append("CM")
			elif num >=500:
				num = num -500
				roman.append('D')
			elif num >= 400:
				num = num -400
				roman.append('CD')
			elif num >=100:
				num = num - 100
				roman.append('C')
			elif num >= 90:
				num = num -90
				roman.append('XC')
			elif num >= 50:
				num = num - 50
				roman.append('L')
			elif num >= 40:
				num = num - 40
				roman.append('XL')
			elif num >= 10:
				num = num - 10
				roman.append('X')
			elif num >= 9:
				num = num - 9
				roman.append('IX')
			elif num >= 5:
				num = num - 5
				roman.append('V')
			elif num >= 4:
				num = num - 4
				roman.append('IV')
			else:
				roman.append('I'*num)
				break
		return ''.join(roman)

if __name__ == '__main__':
	s = Solution()
	rom = s.intToRoman()
	