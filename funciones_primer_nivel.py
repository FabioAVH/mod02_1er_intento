#"Programacion funcional", donde le pueden enviar funciones como paramentros de otras funciones

def normal(x):
    return x

def cuadrado(x):
    return x*x

def SumaTodos(limitTo, f): #funcion de primer nivel, porque acepta funciones como parametros
    resultado=0
    for i in range(limitTo+1):
        resultado += f(i)
    return resultado

print(SumaTodos(100, normal))
print(SumaTodos(3,cuadrado))