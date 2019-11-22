class Solution(object):
	def generateParenthesis(self, n):
		ans = []
		def generate(A = []):
			if len(A) == 2*n:
				if isValid(A):
					ans.append("".join(A))
			else:
				A.append("(")
				generate(A)
				A.pop()
				A.append(")")
				generate(A)
				A.pop()
		def isValid(A):
			bal = 0
			for c in A:
				if c == "(":
					bal += 1
				else:
					bal -= 1
				if bal < 0:
					return False
			return bal == 0

		generate()
		print 'ans: ',ans
		return ans
	def generateParenthesis(self, N):
		ans = []
		def backtrack(S = '', left = 0, right = 0):
			print 'backtrack: S = {},left = {},right = {}'.format(S,left,right)
			if len(S) == 2 * N:
				ans.append(S)
				return
			if left < N:
				backtrack(S+'(', left+1, right)
			if right < left:
				backtrack(S+')', left, right+1)

		backtrack()
		return ans
	def generateAll(self,n,A = []):
		if len(A) == 2*n:
			print 'ansower',A
		else:
			A.append('(')
			self.generateAll(3,A)
			A.pop()
			A.append(")")
			self.generateAll(3,A)
			A.pop()
		

if __name__ == '__main__':
	s = Solution()
	s.generateParenthesis1(3)