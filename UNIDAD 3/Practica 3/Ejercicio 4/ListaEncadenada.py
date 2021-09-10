
import re


class Nodo:
    __elem=None
    __sig=None

    def __init__(self,elemento=None) -> None:
        self.__elem=elemento
        self.__sig=None
    
    def setElem(self,elemento):
        self.__elem=elemento
    def setSig(self,siguiente):
        self.__sig=siguiente
    def getSig(self):
        return self.__sig
    def getElem(self):
        return self.__elem

class ListaEncadenada:
    __cab=None
    __tope=None

    def __init__(self) -> None:
        self.__cab=None
        self.__tope=0
    
    def vacia(self):
        return self.__tope==0
    def getTope(self):
        return int(self.__tope)
    def insertar(self,posicion,elemento):
        if (posicion > 0)and(posicion <= self.__tope + 1):
                nuevo=Nodo(elemento)
                if self.__cab == None:
                    nuevo.setSig(self.__cab)
                    self.__tope+=1
                    self.__cab=nuevo
                elif posicion==1:

                    nuevo.setSig(self.__cab)
                    self.__tope+=1
                    self.__cab=nuevo
                else: 
                        i=1
                        aux=self.__cab
                        ant=self.__cab
                        while i!=posicion:
                            ant=aux
                            aux=aux.getSig()
                            i+=1
                        nuevo.setSig(aux)
                        ant.setSig(nuevo)
                        self.__tope+=1
        else:
            print('ERROR: posicion {} inexistente en la lista'.format(posicion))

    def insertarContenido(self,elemento):
        if self.lleno():
            nuevo=Nodo(elemento)
            if self.__cab == None:
                nuevo.setSig(self.__cab)
                self.__tope+=1
                self.__cab=nuevo
            else:
                i=1
                aux=self.__cab
                ant=self.__cab
                while i<self.__tope+1 and aux.getElem()<elemento:
                    ant=aux
                    aux=aux.getSig()
                    i+=1
                if i==1:
                    nuevo.setSig(aux)
                    self.__tope+=1
                    self.__cab=nuevo
                else:
                    nuevo.setSig(aux)
                    ant.setSig(nuevo)
                    self.__tope+=1
        else:
            print('ERROR: lista llena')
        


    def suprimir(self,posicion):
            if (posicion > 0)and(posicion <= self.__tope):
                i=1
                aux=self.__cab
                ant=self.__cab
                while i!=posicion:
                    ant=aux
                    aux=aux.getSig()
                    i+=1
                if i==1:
                    self.__cab=aux.getSig()
                else:
                    ant.setSig(aux.getSig())
                self.__tope -= 1
            else:
                print('ERROR: posicion no valida')
    
    def recuperar(self,posicion):
            retorna=None
            if (posicion > 0)and(posicion <= self.__tope):
                i=1
                aux=self.__cab
                while i!=posicion:
                    aux=aux.getSig()
                    i+=1
                retorna = aux.getElem()
                    
            else:
                print('ENTRO ACA')
                print('ERROR: posicion no valida')
                retorna = False
            return retorna

    def recorrer(self):
        if not self.vacia():
            aux=self.__cab
            if aux!=None:
                aux=aux.getSig()
                while aux!=None:
                    print(aux.getElem())
                    aux=aux.getSig()
        else:
            print('LISTA VACIA')


    def primerElemento(self):
        if not self.vacia():
            return self.__cab.getElem()
        else:
            print('ERROR:La lista esta vacia')
            input('Presione para continuar...')

    def ultimoElemento(self):
        if not self.vacia():
            aux=self.__cab
            ant=self.__cab
            while aux!=None:
                ant=aux
                aux=aux.getSig()
            return ant.getElem()
        else:
            print('ERROR:La lista esta vacia')
            input('Presione para continuar...')