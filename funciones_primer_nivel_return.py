def MaxNum(*lista):
    
    if len(lista) == 0:
        return 0
    
    m = lista[0]
    
    for i in range(1,len(lista)):
        if lista[i] > m:
            m=lista[i]
            
    return m

def MinNum(*lista):
    
    if len(lista) == 0:
        return 0
    
    m = lista[0]
    
    for i in range(1,len(lista)):
        if lista[i] < m:
            m=lista[i]
            
    return m


def Media(*lista):
    
    if len(lista) == 0:
        return 0
    
    m = lista[0]
    
    for i in range(1,len(lista)):
        m+=lista[i]
            
    return m/len(lista)

funciones = {
    'max': MaxNum,
    'min': MinNum,
    'med': Media
    }


def ReturnFunc(nombre):
    nombre=nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    return None

#Si quiero que se ejecute la funcion que llave con ReturnFunc debo escribir:
#ReturnFunc('max')(3,6,9,12) por ejemplo