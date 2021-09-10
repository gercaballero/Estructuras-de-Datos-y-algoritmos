import numpy as np
class ListaSecPosicion:
    __items=None
    __tope=0
    __cant=0
    def __init__(self,xcant):
        self.__items= np.empty(xcant,dtype=int)
        self.__tope=0
        self.__cant= xcant

    def tope(self):
        return self.__tope
    def vacia(self):
        return self.__tope == 0
    def insertar(self,posicion,elemento):
        if (posicion > 0)and(posicion <= self.__tope + 1):
            for i in range(self.__tope, posicion - 1, -1):
                self.__items[i] = self.__items[i-1]
            self.__items[posicion - 1]=elemento
            self.__tope += 1
    def recorrer(self):
        if not self.vacia():
            for i in range(self.__tope):
                print(self.__items[i])
        else:
            print('ERROR:No se puede recorrer,la lista esta vacia')
    
    def suprimir(self,posicion):
        if not self.vacia():
            if (posicion > 0)and(posicion <= self.__tope):
                rec=self.__items[posicion - 1]
                for i in range(posicion - 1,self.__tope - 1):
                    self.__items[i]=self.__items[i+1]
                self.__tope -= 1
                return rec
            else:
                print('ERROR:No existe posicion {} en la lista',posicion)
                input('Presione para continuar...')
        else:
            print('ERROR:La lista esta vacia')
            input('Presione para continuar...')

    def recuperar(self,posicion):
        if not self.vacia():
            if (posicion > 0)and(posicion <= self.__tope):
                return self.__items[posicion-1]
            else:
                print('ERROR:No existe posicion {} en la lista',posicion)
        else:
            print('ERROR:La lista esta vacia')

    def buscar(self,elemento):
        posicion=False
        if not self.vacia():
            i=0
            while i<self.__tope-1 and self.__items[i]!=elemento:
                i+=1
            if i<self.__tope-1:
                posicion=i+1
        return posicion

    def primerElemento(self):
        if not self.vacia():
            return self.__items[0]
        else:
            print('ERROR:La lista esta vacia')
            input('Presione para continuar...')

    def ultimoElemento(self):
        if not self.vacia():
            return self.__items[self.__tope - 1]
        else:
            print('ERROR:La lista esta vacia')
            input('Presione para continuar...')



