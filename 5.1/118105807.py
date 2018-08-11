from math import sqrt

n = input()
cut = int( sqrt( n ) )
originalList = range( 3, n+1, 2 )
copyOg = list( originalList )
atualLista = list()
originalSize = len( originalList )
cortados = list()

print originalList
print cut

if cut % 2 == 0:
	cut -= 1

i = 0
saltos = originalList[i]

while saltos < cut:
	k = saltos * saltos
	pos = ( k - 3 ) / 2
	cortadosAtual = list()
	
	print saltos, k, pos
	
	while pos < originalSize:
		cortados.append( originalList[pos] )
		cortadosAtual.append( originalList[pos] )
		copyOg[pos] = 0
		pos = pos + saltos
	
	atualLista = filter( lambda a: a != 0, copyOg )
	print cortadosAtual
	print atualLista
	

	i += 1
	saltos = originalList[i]

atualLista.insert( 0, 2 )
print atualLista

