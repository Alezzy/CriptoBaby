nn = input()

def mdc( dividendo, divisor ):
	aux = dividendo
	while divisor > 0:
		dividendo = divisor
		divisor = aux % divisor
		aux = dividendo
	return dividendo

while nn > 0:
	n = input()
	l = list()
	m = 2
	l.append( 1 )

	while m <= n:
		if mdc( n, m ) == 1:
			l.append( m )
		m += 1

	print l
	
	print "---"
	nn -= 1
