n = input()

while n > 0:
	d1, mod = input()
	cmod = mod
	mdc = 0
	x0, y0 = 1, 0
	x1, y1 = 0, 1
	print d1, "-", x0, y0
	print mod, "-", x1, y1
	aux = d1
	while mod > 0:
		d1 = mod
		quociente = aux / d1
		mdc = mod
		mod = aux % mod
		x = x0 - x1 * quociente
		y = y0 - y1 * quociente
		x0 = x1
		y0 = y1
		x1 = x
		y1 = y
		if mod == 0:
			x = y = "-"
		print mod, quociente, x, y
		aux = d1
	if mdc == 1:
		inverso = x0 % cmod
		print inverso
	else:
		print 0
	print "---"
	n -= 1
