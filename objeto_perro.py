#PERRO es la clase principal
class Perro():

    #ATRIBUTOS
    def __init__ (self, n, e, p):
        self.nombre =  n
        self.edad = e
        self.peso = p
        
    #METODOS    
    #el primer parametro debe ser la propia clase, por se objetos c (clase),s (self) o me. Por convenio de usa self
    #El primer parametro permite que se invoque como una instancia salchicho.ladrar()
    #El primer parametro no hay que meterlo, pero el segundo si. Estos cuando los metodos tienen parametros
    def Ladrar(self): #puedo incluir mas parametros
        
        if self.peso >= 8:
            print('GUAU, GUAU !')
        else:
            print('ay, ay !')
        
    #Si escribimos el comando print(salchico) de salchicho = Perro('Miko',3,10)
    def __str__(self):
        return 'Perro {} edad {} peso {}'.format(self.nombre, self.edad, self.peso)


#HERENCIAS
class PerroAsistencia(Perro):
    def __init__ (self, n, e, p, amo):
        Perro.__init__(self, n, e, p)
        self.amo = amo
        self.__trabajando = False #atributo privado '__nombre'. Es una simulacion. No lo puedo acceder directamente
        
    def __str__(self):
        return 'Perro de asistencia de {}'.format(self.amo)
    
    def Pasear(self):
        return '{} ayudo a mi amo {} a pasear'.format(self.nombre, self.amo)
    
    def Ladrar(self):
        if self.__trabajando:
            print('Shhhh no puedo labrar')
        else:
            Perro.Ladrar(self) #se debe incluir la instancia self
    
    def Trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
    
    