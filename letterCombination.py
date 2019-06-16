class Solution(object):
	digit_to_letter = {
		'2': ['a','b','c'],
		'3':['d','e','f'],
		'4':['g','h','i'],
		'5':['j','k','l'],
		'6':['m','n','o'],
		'7':['p','q','r','s'],
		'8':['t','u','v'],
		'9':['w','x','y','z'],
		}
	#1: use reduce function
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		letters = []
		if not digits:
			return []
		for digit in digits:
			letter = self.digit_to_letter[digit]
			letters.append(letter)
		return self.list_combination(letters)

	def list_combination(self,lists):

		def myfunc(list1, list2):
			return [str(i)+str(j) for i in list1 for j in list2]
		#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
		return reduce(myfunc, lists)

	#2 use backtrack alogrithm
	def backtrack(self,combination, next_digits):
		# if there is no more digits to check
		if len(next_digits) == 0:
			# the combination is done
			output.append(combination)
		# if there are still digits to check
		else:
			# iterate over all letters which map 
			# the next available digit
			letters = self.digit_to_letter[next_digits[0]].
			for letter in letters:
				# append the current letter to the combination
				# and proceed to the next digits
				backtrack(combination + letter, next_digits[1:])

if __name__ == '__main__':
	s = Solution()
	print 'AA: ',s.letterCombinations('23')





