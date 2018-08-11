nn = input()

while nn > 0:
	n, b = input()
	q = n - 1
	k = 0
	while q % 2 == 0:
		k += 1
		q = q / 2
	print k, q
	R, A, E, I = 1, b, q, 'S'
	print R, A, E, I
	R = ( R * A ) % n
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
	print q, R
	antn = n - 1
	pot = R % n
	if pot == 1 or pot == antn:
		print "INCONCLUSIVO"
	else:
		pot = R
		e = q
		while k > 1:
			pot = ( pot * pot ) % n
			e = e * 2
			print e, pot
			if pot == antn:
				print "INCONCLUSIVO"
				break
			k -= 1
		if k == 1:
			print "COMPOSTO"
	print "---"
	nn -= 1
