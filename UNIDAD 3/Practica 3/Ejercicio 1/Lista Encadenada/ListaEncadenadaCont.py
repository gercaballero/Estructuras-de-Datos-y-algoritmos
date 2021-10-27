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

    def __init__(self,xcant) -> None:
        self.__cant=xcant
        self.__cab=None
        self.__tope=0
    
    def vacia(self):
        return self.__tope==0
    def getTope(self):
        return self.__tope

    def insertar(self,elemento):
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
    def suprimirCont(self,elemento):
        if not self.vacia():
            aux = self.__comienzo
            ant = self.__comienzo
            while aux != None and aux.getDato() != elemento:
                ant = aux
                aux = aux.getSiguiente()

            #Elimina la cabeza
            if aux == self.__comienzo:
                self.__comienzo = aux.getSiguiente()
            #No se encontro el elemento
            elif aux == None:
                print("Elemento no encontrado")
            #Encadenamiento entre anterior y siguiente al nodo con el elemento a eliminar
            else:
                ant.setSiguiente(aux.getSiguiente())
            self.__tope -= 1
            del aux
        else:
            print("Lista vacia")
    def recuperar(self,posicion):
        if not self.vacia():
            if (posicion > 0)and(posicion <= self.__tope):
                i=1
                aux=self.__cab
                ant=self.__cab
                while i!=posicion:
                    ant=aux
                    aux=aux.getSig()
                    i+=1
                if i==posicion:
                    return aux.getElem()
                    
            else:
                print('ERROR: posicion no valida')
                return False
        else:
            print('ERROR:La lista esta vacia')

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