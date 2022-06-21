def éfibonacci(x):
	n=0
	n_2=1
	l=[0]
	while n<x:
            n_antigo=n
            n=n_2
            n_2=n_2+n_antigo
            l.append(n)

	if n==x:
	    print('{} faz parte da sequência de Fibonnaci, que até esse ponto é \n {}'.format(x,l))
	else:
	    print('{} não faz parte da sequência de Fibonnaci, que do início até imediatamente depois desse esse ponto é \n {}'.format(x,l))
