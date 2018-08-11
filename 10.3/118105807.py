from math import sqrt
from collections import OrderedDict

def mdc( dividendo, divisor ):
	aux = dividendo
	while divisor > 0:
		dividendo = divisor
		divisor = aux % divisor
		aux = dividendo
	return dividendo

def inverso( d1, mod ):
	cmod = mod
	mdc = 0
	x0, y0 = 1, 0
	x1, y1 = 0, 1
	aux = d1
	while mod > 0:
		d1 = mod
		quociente = aux / d1
		mdc = mod
		mod = aux % mod
		x = x0 - x1 * quociente
		y = y0 - y1 * quociente
		x0 = x1
		y0 = y1
		x1 = x
		y1 = y
		if mod == 0:
			x = y = "-"
		aux = d1
	if mdc == 1:
		inverso = x0 % cmod
		return inverso
	return 0

def U( n ):
	l = list()
	m = 2
	l.append( 1 )

	while m <= n:
		if mdc( n, m ) == 1:
			l.append( m )
		m += 1

	return l

nn = input()

while nn > 0:
	num, sub = input()
	
	u = U( num )
	
	#3
	if 1 not in sub:
		print "NAO"
		print "---"
		nn -= 1
		continue

	#1
	if not set( sub ).issubset( u ) :
		print "NAO"
		print "---"
		nn -= 1
		continue

	#2
	cb = False
	for elem in sub:
		for elem2 in sub:
			h = ( elem * elem2 ) % num
			if h  not in sub:
				cb = True
				break
		if cb:
			break
	if cb:
		print "NAO"
		print "---"
		nn -= 1
		continue
	
	#4
	cb2 = False
	for elem in sub:
		i = inverso( num, elem )
		h = ( elem * i ) % num
		if h not in sub:
			cb2 = True
			break
	if cb:
		print "NAO"
		print "---"
		nn -= 1
		continue
	
	print "SIM"
	print "---"
	nn -= 1
