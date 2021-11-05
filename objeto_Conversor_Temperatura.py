#Este es un objeto un poco inutil, pero sirve de ejemplo

#Nota: yo puedo con '__' hacer que un proceso sea privado como con las variables

class Termometro():
    
    def __init__(self):
        self.__Unidad = 'C' # con el __ los hacemos privados
        self.__Temperatura = 0
        
    def __str__(self):
        return '{} grados {}'.format(self.__Temperatura, self.__Unidad)
    
    
    def __Conversor(self, Temperatura, Unidad): #con el __ hemos definido esta funcion como privada
        if Unidad == 'C':
            return '{} grados F'.format(Temperatura * 9/5 + 32)
        elif Unidad == 'F':
            return '{} grados C'.format((Temperatura - 32)*5/9)
        else:
            return 'Unidad incorrecta'
        
    #El siguiente tipo de funciones es para hacer 'set' y 'get' de la variable (Getter y Setter)
    def unidadMedida(self,uniM=None):
        if uniM == None:
            return self.__Unidad
        else:
            if uniM == 'F' or uniM == 'C':
                self.__Unidad = uniM
                
    def temp(self,uniT=None):
        if uniT == None:
            return self.__Temperatura
        else:
            self.__Temperatura = uniT
                
    
    #Funciones operativas
    def mide(self,uniM=None):
        if uniM == None or uniM == self.__Unidad:
            return self.__str__()
        else:
            if uniM == 'F' or uniM == 'C':
                return self.__Conversor(self.__Temperatura, self.__Unidad)
            else:
                return self.__str__()
        