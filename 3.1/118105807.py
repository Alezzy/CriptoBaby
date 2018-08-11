n = input()
while n > 0:
	dividendo, divisor = input()
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
	print "---"
	n = n - 1
