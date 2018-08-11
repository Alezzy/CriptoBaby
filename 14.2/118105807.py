nn = input()

def power( A, E, mod ):
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

while nn > 0:
	p, a, s, t = input()

	puma = p - 1 - a
	m = power( s, puma, p )
	m = m * t % p
	print m

	print "---"
	nn -= 1

