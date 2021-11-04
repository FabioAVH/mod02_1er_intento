#La recursividad es un elegante pero poco eficiente. Siempre tiene que haber una condicion de parada
#de lo contrario tiene a infito


def retroContador(t):
        print('{} , '.format(t), end='')
        
        if t > 0:
            retroContador(t-1)

retroContador(10)