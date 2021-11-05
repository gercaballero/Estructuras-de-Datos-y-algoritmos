import numpy as np

class TablaHash:

    def __init__(self, cantDatos,primo=True): #el parametro primo permite decir si el tamaño sera primo o no
        if primo:
            cantDatos = self.buscarPrimo(int(cantDatos/0.7))
        self.__tabla= np.empty(cantDatos) 
        for i in range (len(self.__tabla)):
            self.__tabla[i]=0

    def funcionHash(self,clave):
        return clave % len(self.__tabla)

    def insertar(self,clave):
        dir = self.funcionHash(clave)
        i=0
        while self.__tabla[dir]!=0 and i<self.getTamano() and self.__tabla[dir]!=clave:
            dir = (dir+1) % len(self.__tabla)
            i+=1
        if i == self.getTamano():
            print('ERROR: tabla saturada')
        elif self.__tabla[dir]==clave:
            print('ERROR: elemento ya insertado')
        else:  
            self.__tabla[dir]=clave

    def buscarPorPosicion(self,pos):
        result = None
        if pos >= 0 and pos < self.getTamano() :
            result = self.__tabla[pos]
        return result
    def buscar(self,clave):
        i=0
        dir = self.funcionHash(clave)
        aux = dir
        while self.__tabla[dir]!=clave and i<self.getTamano() and self.__tabla[dir]!=0:
            dir = (dir+1) % len(self.__tabla)
            i+=1
        if i<self.getTamano() and self.__tabla[dir]!=0:
            print('Se encontro la clave, con direccion {}'.format(dir))
            print('La longitud de la secuencia de prueba al buscar la clave {} es {}'.format(clave,i))
            return dir
        else: 
            print('No se encontro la clave')
            return None
        
            
    def getTamano(self):
        return int(len(self.__tabla))
    def mostrarTabla(self):
        print(self.__tabla)



    '''--------------VERIFICACION DE PRIMOS--------------'''
    def esPrimo(self,numero):
        if numero <= 2:
            return False
        for i in range(2, numero): 
            if numero % i == 0:
                return False
        return True
    def buscarPrimo(self,numero):
        while not self.esPrimo(numero):
            numero+=1
        return numero