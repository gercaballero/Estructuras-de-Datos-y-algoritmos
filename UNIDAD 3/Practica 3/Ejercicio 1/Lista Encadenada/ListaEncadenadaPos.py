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

class ListaEncadenadaPos:
    __cab=None
    __tope=None

    def __init__(self,xcant) -> None:
        self.__cant=xcant
        self.__cab=None
        self.__tope=0
    
    def vacia(self):
        return self.__tope==0
    def getTope(self):
        return self.__tope
    
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

    def suprimir(self,posicion):
        if not self.vacia():
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
            else:
                print('ERROR: posicion no valida')
    
    def recuperar(self,pos):
        result = None
        if pos > 0 and pos <= self.__tope:
            aux = self.__comienzo
            i = 1
            while i < pos:
                aux = aux.getSiguiente()
                i += 1
            result = aux.getDato()
        return result

    def recorrer(self):
        lista='['
        aux=self.__cab
        if aux!=None:
            lista+=str(aux.getElem())
            aux=aux.getSig()
            while aux!=None:
                lista+=','
                lista=lista+str(aux.getElem())
                aux=aux.getSig()
        lista=lista+']'
        print(lista)

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