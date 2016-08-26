import sys

def downtrianle(arg):
    n = int(arg)
    i = 0  # Multiplicador para las sangrias
    while 0 < n:
        j = 2 * i  # Calculo el numero de espacios de sangria a imprimir en la linea
        while (0 < j):
            print "",
            j -= 1
        s = 2*n-1  # s = numero de "*" a imprimir en cada linea
        while(s > 0):
            print "*",
            s -= 1
        print "\n"  # Imprimo el salto de linea
        i += 1
        n -= 1

downtrianle(sys.argv[1])