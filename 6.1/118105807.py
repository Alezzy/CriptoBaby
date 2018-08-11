n = input()

while n > 0:
	n1, n2, mod = input()
	rn1 = n1 % mod
	rn2 = n2 % mod
	rsum = ( rn1 + rn2 ) % mod
	rsub = ( rn1 - rn2 ) % mod
	rprod = ( rn1 * rn2 ) % mod
	print rn1, rn2, rsum, rsub, rprod
	print "---"
	n -= 1

