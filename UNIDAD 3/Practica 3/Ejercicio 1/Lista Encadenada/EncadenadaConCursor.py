import numpy as np

class Nodo:
    __dato=None
    __sig=None

    def __init__(self) -> None:
        self.__dato=None
        self.__sig=-2 #equivale a null
    
    def setDato(self,elemento):
        self.__dato=elemento

    def getDato(self):
        return self.__dato
    
    def setSiguiente(self,siguiente):
        self.__sig=siguiente
    
    def getSiguiente(self):
        return self.__sig

class ListaEncadenadaConCursores:
    __max=None
    __cab=None
    __cant=None
    __espacio=None
    __disponible=None

    def __init__(self,xmax) -> None:
        self.__max=xmax
        self.__cab=0
        self.__cant=0
        self.__espacio=np.empty(xmax,dtype=Nodo)
        for i in range(self.__max):
            self.__espacio[i]=Nodo()
        self.__disponible=0
    def vacia(self):
        return self.__cant==0

    def getDisponible(self):
        i=0
        while i<self.__max and self.__espacio[i].getSiguiente()!=-2 :
            i+=1
        if i<self.__max:
            self.__disponible=i
            return True
        else:
            disp=-2
            return False
            
    def freeDisponible(self,disp):
        if disp>=0 and disp<self.__max:
            self.__espacio[disp].setSiguiente(-2)
            return True
        else:
            return False

    def insertar(self,posicion,x):
        if self.__cant<self.__max and posicion>0 and posicion<=self.__cant+1 and self.getDisponible():
                self.__espacio[self.__disponible].setDato(x)
                ant=self.__cab
                cabeza=self.__cab
                i=0
                while i<posicion-1:
                        i+=1
                        ant=cabeza
                        cabeza=self.__espacio[cabeza].getSiguiente()
                if cabeza==self.__cab:
                        if self.__cant==0:
                                self.__espacio[self.__cab].setSiguiente(-1)
                        else:
                                self.__espacio[self.__disponible].setSiguiente(self.__cab)
                        self.__cab=self.__disponible
                elif cabeza ==-1:
                        self.__espacio[self.__disponible].setSiguiente(-1)
                        self.__espacio[ant].setSiguiente(self.__disponible)
                else:
                        self.__espacio[self.__disponible].setSiguiente(cabeza);
                        self.__espacio[ant].setSiguiente(self.__disponible);                
                self.__cant+=1
                return True
        else:
                print('ERROR: Espacio lleno o posicion incorrecta')
                return False
    def insertarContenido(self,x):
        if self.__cant<self.__max and self.getDisponible():
                ant=self.__cab
                cabeza=self.__cab
                i=0
                self.__espacio[self.__disponible].setDato(x)
                while i<self.__cant and cabeza!=-1 and self.__espacio[cabeza].getDato()<x:
                        i+=1
                        ant=cabeza
                        cabeza=self.__espacio[cabeza].getSiguiente()
                if cabeza ==self.__cab:
                        if self.__cant==0:
                                self.__espacio[self.__cab].setSiguiente(-1)
                        else:
                                self.__espacio[self.__disponible].setSiguiente(self.__cab)
                        self.__cab=self.__disponible
                elif cabeza==-1:
                        self.__espacio[self.__disponible].setSiguiente(-1)
                        self.__espacio[ant].setSiguiente(self.__disponible)
                else:
                        self.__espacio[self.__disponible].setSiguiente(cabeza)
                        self.__espacio[ant].setSiguiente(self.__disponible)
                self.__cant+=1
                return True
        else:
                print('ERROR: Espacio lleno')
                return False
    def suprimir(self,posicion):
                if self.__cant!=0 and posicion>0 and posicion<self.__cant+1:
                        ant=self.__cab
                        cabeza=self.__cab
                        i=0
                        while i<posicion-1 and cabeza!=-1:
                                i+=1
                                ant=cabeza
                                cabeza=self.__espacio[cabeza].getSiguiente()
                        if cabeza==self.__cab:
                                if self.__cant==1:
                                        self.__cab=0
                                else:
                                        self.__cab=self.__espacio[ant].getSiguiente()
                        else:
                                self.__espacio[ant].setSiguiente(self.__espacio[cabeza].getSiguiente())
                        x=self.__espacio[cabeza].getDato()
                        self.__disponible=cabeza
                        self.freeDisponible(self.__disponible)
                        self.__cant-=1
                        return x
                else:
                        print('ERROR: Lista vacía o posición incorrecta.')
                        return False

    def recorrer(self):
        print('-'*(self.__cant*5))
        lista='['
        if self.__cant!=0:
                aux=self.__espacio[self.__cab]
                lista+=str(aux.getDato())
                while aux.getSiguiente()!=-1:
                        lista+=','
                        aux=self.__espacio[aux.getSiguiente()]
                        lista=lista+str(aux.getDato())
        lista=lista+']'
        print(lista)
            
                        