from math import sqrt
n = input()
while n > 0:
	num = input()
	x = int( sqrt( num ) )
	y = 0
	while num != ( x*x - y*y ):
		print x, y, 'N'
		x = x+1
		y = int( sqrt( x*x - num ) )
	print x, y, 'S'
	print x-y, x+y
	print "---"
	n -= 1

