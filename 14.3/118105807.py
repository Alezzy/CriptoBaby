from math import sqrt, ceil

nn = input()

def inverse( dividendo, divisor ):
	x0, y0 = 1, 0
	x1, y1 = 0, 1
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
		aux = dividendo
	return x0

while nn > 0:
	g, h, p = input()

	m = int( ceil( sqrt( p - 1 ) ) )
	print m

	j = 0
	b = []

	while j < m:
		s = ( g ** j ) % p
		b.append( s )
		print j, s
		j += 1

	invg = inverse( g, p ) % p
	t = ( invg ** m ) % p

	i = 0
	while i < m:
		s = ( h * ( t ** i ) ) % p
		print i, s
		if s in b:
			j = b.index( s )
			x =  ( ( i * m ) + j )
			print i, j
			print x
			break
		i += 1

	print "---"
	nn -= 1
