import numpy as np   ##Relacion de orden
class Lista:
    __items=None
    __tope=0
    __cant=0
    def __init__(self,xcant,tipo=int):
        self.__items= np.empty(xcant,dtype=tipo)
        self.__tope=0
        self.__cant= xcant
    def vacia(self):
        return self.__tope == 0
    def llena(self):
        return self.__tope == self.__cant
    def insertar(self,elemento):
        if not self.llena():
            if self.__tope == 0:
                self.__items[0]= elemento
                self.__tope += 1
            else:
                i=0
                while i < self.__tope and elemento < self.__items[i]:
                    i+=1
                for j in range(self.__tope, i, -1):
                    self.__items[j]= self.__items[j-1]
                self.__items[i]= elemento
                self.__tope += 1
        else:
            print('ERROR:lista llena. No se puede ingresar el numero {}'.format(elemento))
    def suprimir(self,elemento):
        if self.vacia():
            print('ERROR:La lista esta vacia')
            input('Presione para continuar...')
        else:
            i=0
            while i<self.__tope and elemento != self.__items[i]:
                i+=1
            if i <self.__tope:
                aux=self.__items[i]
                for j in range(i,self.__tope):
                    self.__items[j]=self.__items[j+1]
                self.__tope -= 1
                return aux
            else:
                print("ERROR: El elemento {} no se encuetra en la lista".format(elemento))
    
    def buscar(self,elemento):
        pos=False
        if not self.vacia():
            i=0
            while i<self.__tope-1 and self.__items[i]!=elemento:
                i+=1
            if i<self.__tope-1:
                pos=i+1
        else:
            print('ERROR: La lista esta vacia')
        return pos
    
    def recorrer(self):
        for i in range(self.__tope):
            print(self.__items[i])
    
    def primerElemento(self):
        if self.vacia() == False:
            return self.__items[0]
        else:
            print('ERROR:La lista esta vacia')
            input('Presione para continuar...')
    def ultimoElemento(self):
        if self.vacia() == False:
            return self.__items[self.__tope - 1]
        else:
            print('ERROR:La lista esta vacia')
            input('Presione para continuar...')

