nn = input()

def F( num ):
	return ( 2 ** ( 2 ** num ) ) + 1

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

while nn > 0:
	num = input()
	fermat = F( num )
	antfermat = fermat - 1
	print fermat
	R = pot( 5, antfermat / 2, fermat )
	
	result = R
	if result == antfermat:
		print "PRIMO"
	else:
		print "COMPOSTO"
	print "---"
	nn -= 1
