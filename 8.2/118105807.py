from math import sqrt
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

nn = input()

while nn > 0:
	n = input()
	antn = n - 1
	factors = get_factors( n )
	carmichael = "SIM"
	if len( factors ) > 1:
		for factor in factors:
			df = factor * factor
			if n % df == 0:
				carmichael = "NAO"
				break
			antf = factor - 1
			if antn % antf != 0:
				carmichael = "NAO"
				break
	else:
		carmichael = "NAO"
	print carmichael
	print "---"
	nn -= 1
