n = input()
while n > 0:
	passos = 0
	dividendo, divisor = input()
	sub = dividendo
	while sub >= 0:
		print passos, sub
		sub = sub - divisor
		passos = passos + 1
	print "---"
	n = n - 1
