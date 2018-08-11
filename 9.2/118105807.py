from math import sqrt, pow
from collections import OrderedDict

def get_factors( num ):
	factors = dict()
	menorFator = int( sqrt( num ) )+1
	while num > 1:
		i = 2
		for i in xrange( 2, menorFator+1 ):
			if num % i == 0 :
				if i in factors:
					factors[i] += 1
					num /= i
					break
				else:
					factors[i] = 1
					num /= i
					break
		if i == menorFator and num > 1:
			factors[num] = 1
			break;
	orderedFactors = OrderedDict( sorted( factors.items() ) )
	for factor, mult in orderedFactors.items():
		print factor, mult
	return orderedFactors.keys()

def euclides( dividendo, divisor ):
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
	return x0, y0

def noveUm( cong, mods ):
	i = 1
	a, b = cong[0], cong[1]
	m, n = mods[0], mods[1]
	while i < len( mods ):
		alpha, beta = euclides( m, n )
		print alpha, beta
		i += 1
		mn = m * n
		a = ( ( a * beta * n ) + ( m * alpha * b ) ) % mn
		m = mn
		print a, mn
		if i < len( mods ):
			n = mods[i]
			b = cong[i]

def seteDois( A, E, p ):
	print E
	return E % ( p - 1 )

def seisDois( A, E, mod ):
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

nn = input()

while nn > 0:
	base, exp, mod = input()
	factors = get_factors( mod )
	cong, mods = [], []
	for factor in factors:
		if base % factor == 0:
			cong.append( 0 )
			mods.append( factor )
			print 0
		else:
			fermat = factor - 1
			newExp = exp % fermat
			resto = ( base ** newExp ) % factor
			cong.append( resto )
			mods.append( factor )
			e = seteDois( base, newExp, factor )
			seisDois( base, e, factor )
	noveUm( cong, mods )
	print "---"
	nn -= 1
