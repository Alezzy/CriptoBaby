from math import sqrt

n = input()
nums = []
max_div = 0

for i in xrange( 1, n+1 ):
	sumDiv = 1 + ( sum( [i % d == 0 for d in xrange( 2, i + 1 )] ) )
	if sumDiv > max_div:
		max_div = sumDiv
		nums.append(i)

print nums

