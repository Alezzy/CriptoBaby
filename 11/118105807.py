def mdc( dividendo, divisor ):
	aux = dividendo
	while divisor > 0:
		dividendo = divisor
		divisor = aux % divisor
		aux = dividendo
	return dividendo

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
	num = input()

	u = U( num )
	sub = []

	print u

	for unum in u:
		l = []
		l.append( 1 )
		expUnum = 1
		modUnum = unum
		while modUnum != 1:
			if modUnum in u:
				l.append( modUnum )
			expUnum += 1
			modUnum = ( unum ** expUnum ) % num
		l.sort()
		sub.append( l )
	for g in sub:
		print g

	print "---"
	nn -= 1
