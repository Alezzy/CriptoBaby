n = input()
while n > 0:
	dividendo, divisor = input()
	print dividendo
	aux = dividendo
	while divisor >= 0:
		print divisor
		if divisor == 0:
			break
		dividendo = divisor
		divisor = aux % divisor
		aux = dividendo
	print "---"
	n = n - 1
