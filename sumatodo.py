#programa de prueba github

def sumatodos(limit):
    result=0
    for i in range(0,limit+1):
        result += i
    return result

def sumaTodoslosCuadrados(limit):
    resultado=0
    for i in range(limit+1):
        resultado += i*i
    return resultado

print (sumatodos(100)) 
print(sumaTodoslosCuadrados(3))


    