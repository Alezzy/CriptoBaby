from math import sqrt
from collections import OrderedDict

def factors( num ):
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
	return orderedFactors

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

nn = input()

while nn > 0:
	num = input()
	exponents = set()
	n1 = num - 1
	base = 2
	broke2 = False
	if num % 2 == 1:
		facts = factors( n1 )
		for factor, mult in facts.items():
			print factor, mult

		while base < num:
			broke = False
			print base
			exp = n1
			print exp
			m = pot( base, exp, num )
			if m % num == 1:
				for factor, mult in facts.items():
					exp = n1 / factor
					if exp in exponents or base < 3:
						print exp
						m = pot( base, exp, num )
						if m == 1:
							exponents.add( exp )
						if len( exponents ) > 0 and m != 1 and base > 2:
							print "PRIMO"
							broke = True
							break
			if broke:
				broke2 = True
				break
			base += 1
	if not broke2:
		print "COMPOSTO"
	print "---"
	nn -= 1

