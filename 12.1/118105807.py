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

nn = input()

while nn > 0:
	num = input()
	p1 = num - 1
	facts = factors( p1 )
	for factor, mult in facts.items():
		print factor, mult
	k = len( facts )

	i = 1
	g = 1
	for factor, mult in facts.items():
		a = 2
		quocient = p1 / factor
		exp = ( a ** quocient ) % num
		while exp == 1:
			a+=1
			exp = ( a ** quocient ) % num
		h = ( a ** ( p1 / ( factor ** mult ) ) ) % num
		g = ( g * h ) % num
		print factor, a, h
	print g
	print "---"
	nn -= 1
