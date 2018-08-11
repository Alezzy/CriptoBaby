n = input()
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
while n > 0:
	dividendo, divisor, c = input()
	x0, y0 = 1, 0
	x1, y1 = 0, 1
	cpdd = dividendo
	cpds = divisor
	print dividendo, "-", x0, y0
	print divisor, "-", x1, y1
	aux = dividendo
	mdc = 0
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
		else:
			mdc = divisor
		print divisor, quociente, x, y
		aux = dividendo
	if mdc == 0 and cpdd == cpds:
		mdc = cpdd
	if c % mdc == 0:
		cLinha = c / mdc
		xFinal = x0 * cLinha
		yFinal = y0 * cLinha
		print xFinal, yFinal
	else:
		print "0"
	print "---"
	n = n - 1
