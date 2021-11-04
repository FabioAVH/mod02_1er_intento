from functools import reduce

def doble(x):
    return x+x

def esPar(x):
    return x % 2 == 0


lista = [1,3,-1,15,9, 10, 12]

#map, aplica una transformacion a una lista mapeandola
listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(doble, lista)
#multiplica todos los elementos de lista por dos

#filter
listaPares = filter(lambda x: x % 2 == 0, lista)
listaPares1 = filter(esPar, lista)
#filtra los campos pares, es decir, donde el resto de la division del campo en dos es igual a cero (lo que nos
#indica que es par

#reduce, opera todos los valores de la lista y los reduce a uno solo
#requiere un import de functools
sumatorio = reduce(lambda x,y : x+y , lista)

suma100 = reduce(lambda x,y : x+y, range(101))

sumatorioDobles = reduce(lambda x,y : x+y*2, lista)


print(list(listaPares))
print(suma100)

#para copia (clonar) una lista
l = lista[:]
l.insert(0,10) #inserta en la posicion 0, el numero 10
# esto se 
