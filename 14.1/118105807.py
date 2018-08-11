from math import sqrt
nn = input()

def fiEuler( p ):
	return p - 1

def fermat( num ):
	x = int( sqrt( num ) )
	y = 0
	while num != ( x*x - y*y ):
		print x, y, 'N'
		x = x+1
		y = int( sqrt( x*x - num ) )
	print x, y, 'S'
	return x-y, x+y

def power( A, E, mod ):
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

def extendedEuclidian( dividendo, divisor ):
	x0, y0 = 1, 0
	x1, y1 = 0, 1
	print dividendo, "-", x0, y0
	print divisor, "-", x1, y1
	aux = dividendo
	while divisor > 0:
		dividendo = divisor
		quociente = aux / dividendo
		divisor = aux % divisor
		x = x0 - x1 * quociente
		y = y0 - y1 * quociente
		x0 = x1
		y0 = y1
		x1 = x
		y1 = y
		if divisor == 0:
			x = y = "-"
		print divisor, quociente, x, y
		aux = dividendo
	return x0

while nn > 0:
	n, e, b = input()

	# Get 2 prime factors of n
	f1, f2 = fermat( n )
	print f1, f2

	# Get fi( n )
	fiN = fiEuler( f1 ) * fiEuler( f2 )
	print fiN

	# Get the exponent to b^d
	d = extendedEuclidian( e, fiN ) % fiN
	print d

	# ( b^d ) % n
	decrypted = power( b, d, n )
	print decrypted

	print "---"
	nn -= 1
