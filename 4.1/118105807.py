from math import sqrt
from collections import OrderedDict
n = input()
while n > 0:
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
	for factor, mult in orderedFactors.items():
		print factor, mult
	print "---"
	n = n - 1

