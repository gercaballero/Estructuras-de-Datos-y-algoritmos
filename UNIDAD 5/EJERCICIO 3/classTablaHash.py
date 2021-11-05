import numpy as np
import os
from classListaEncadenada import ListaEncadenada
class TablaHash:
    __tabla=None
    def __init__(self, cantDatos,primo=True):
        if primo:
            cantDatos = self.buscarPrimo(int(cantDatos/0.7))
        self.__tabla= np.full(cantDatos,None)


    def funcionDivision(self,clave):
        return clave % len(self.__tabla)
    def funcionHash(self,clave):
        clave= str(clave)
        lista = []
        for i in range(0,len(clave),2): 
            if i+1 < len(clave):
                lista.append(int(clave[i:i+2]))
            else:
                lista.append(int(clave[i]))
        
        dir = sum(lista)

        if dir >= self.getTamano():
            dir = self.funcionDivision(dir)
        return dir
    def insertar(self,clave):
        dir = self.funcionHash(clave)
        i=0
        if self.__tabla[dir] == None:
            self.__tabla[dir] = ListaEncadenada()
        self.__tabla[dir].insertar(clave,0)
        return dir
    
    def buscarPorPosicion(self,pos):
        lista_claves = None
        if pos >= 0 and pos < self.getTamano():
            lista_claves = self.__tabla[pos]
        lista_claves.recorrer()

    def buscarPorClave(self,clave):
        dir = self.funcionHash(clave)   
        if self.__tabla[dir] == None: 
            dir = -1
            ind = -1
        else:
            ind = self.__tabla[dir].buscar(clave)
        return dir, ind
        
            
    def getTamano(self):
        return int(len(self.__tabla))
    def mostrarTabla(self):
        print(self.__tabla)
    def getTabla(self):
        return self.__tabla


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

    def datos(self):
        acum = 0
        cont = 0
        print('{0:^10}{1:^10}'.format('Direcccion','Longitud'))
        for i in range (len(self.__tabla)):
            if self.__tabla[i]!=None:
                print('{0:^10}{1:^10}'.format(i,self.__tabla[i].len()))
            else:
                print('{0:^10}{1:^10}'.format(i,0))
        input()
        os.system('cls')
        for i in range(len(self.__tabla)):
            if self.__tabla[i] != None:

                acum += self.__tabla[i].len()
                cont += 1
        return acum,cont