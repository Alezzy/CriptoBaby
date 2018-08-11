n = input()

while n > 0:
	A, E, p = input()
	E = E % ( p - 1 )
	print E
	R = 1
	ei = 'S'
	if E % 2 == 0:
		ei = 'N'
	print R, A, E, ei
	while E != 0:
		ei = 'S'
		
		if E % 2 != 0:
			R = ( R * A ) % p
			E = ( E - 1 ) / 2
		else:
			E = E / 2
		
		if E % 2 == 0:
			ei = 'N'
		A = ( A * A ) % p
		print R, A, E, ei
	print "---"
	n -= 1
