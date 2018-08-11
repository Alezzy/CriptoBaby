nn = input()

while nn > 0:
	n, b = input()
	R, A, E, I = 1, b, n-1, 'N'
	print R, A, E, I
	while E > 0:
		A = ( A * A ) % n
		E = int( E / 2 )
		if E % 2 == 0:
			I = 'N'
		else:
			I = 'S'
		print R, A, E, I
		if I == 'S':
			R = ( R * A ) % n
	if R == 1:
		print "INCONCLUSIVO"
	else:
		print "COMPOSTO"
	print "---"
	nn -= 1
