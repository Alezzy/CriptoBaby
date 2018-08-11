from math import sqrt

nn = input()

def M( num ):
	return ( 2 ** num ) - 1

def getMaxR( num ):
	p = num / float( 2 )
	r = ( 2 ** p ) - 1
	r = r / ( 2 * num )
	return int( r )

def pot( A, E, mod ):
	R = 1
	ei = 'S'
	if E % 2 == 0:
		ei = 'N'
	print R, A, E, ei
	while E != 0:
		ei = 'S'
		
		if E % 2 != 0:
			R = ( R * A ) % mod
			E = ( E - 1 ) / 2
		else:
			E = E / 2
		
		if E % 2 == 0:
			ei = 'N'
		A = ( A * A ) % mod
		print R, A, E, ei
	return R

while nn > 0:
	p = input()
	mersenne = M( p )
	biggestR = getMaxR( p )
	print mersenne
	print biggestR
	
	primo = True
	for r in xrange( 1, biggestR+1 ):
		q = 1 + ( 2 * r * p )
		print r
		result = pot( 2, p, q )
		if result == 1:
			print q
			primo = False
			break

	if primo:
		print mersenne
	
	print "---"
	nn -= 1
