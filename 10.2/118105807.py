from math import sqrt
from collections import OrderedDict

nn = input()

def fiDeEuler( n, exp ):
	exp -= 1
	return ( n ** exp ) * ( n-1 )

while nn > 0:
	num = input()
	
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
	finalFi = 1
	for factor, mult in orderedFactors.items():
		finalFi *= fiDeEuler( factor, mult )
		print factor, mult

	print finalFi
	print "---"
	nn -= 1
