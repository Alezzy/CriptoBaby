nn = input()

def euclides( dividendo, divisor ):
	x0, y0 = 1, 0
	x1, y1 = 0, 1
	print dividendo, "-", x0, y0
	print divisor, "-", x1, y1
	aux = dividendo
	while divisor > 0:
		dividendo = divisor
		quociente = aux / dividendo
		divisor = aux % divisor
		x = x0 - x1 * quociente
		y = y0 - y1 * quociente
		x0 = x1
		y0 = y1
		x1 = x
		y1 = y
		if divisor == 0:
			x = y = "-"
		print divisor, quociente, x, y
		aux = dividendo
	return x0, y0

while nn > 0:
	cong, mods = input()
	i = 1
	a, b = cong[0], cong[1]
	m, n = mods[0], mods[1]
	while i < len( mods ):
		alpha, beta = euclides( m, n )
		print alpha, beta
		i += 1
		mn = m * n
		a = ( ( a * beta * n ) + ( m * alpha * b ) ) % mn
		m = mn
		print a, mn
		if i < len( mods ):
			n = mods[i]
			b = cong[i]
	print "---"
	nn -= 1
