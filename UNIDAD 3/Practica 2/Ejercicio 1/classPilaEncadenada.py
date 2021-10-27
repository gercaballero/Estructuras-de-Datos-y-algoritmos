class PilaSecuencial:
    __items=[]
    __tope=None
    __cant=None

    def __init__(self,cant=0) -> None:
        self.__items=[]
        self.__cant=cant
        self.__tope=-1

    def vacia(self):
        vacia=False
        if self.__tope==-1:
            vacia=True
        return vacia
    def insertar(self,item):
        if self.__tope< (self.__cant-1):
            self.__items[self.__tope+1]
            self.__tope=self.__tope+1
            return item
        else:
            return 0
        
    def suprimir(self):
        if(self.vacia()):
            return None
        else:
            x = self.__items.pop()
            self.__tope = self.__tope - 1
            return x

class Nodo:
    __item=None
    __siguiente=None
    def __init__(self) -> None:
        self.__item=None
        self.__siguiente=None
    
    def obtenerItem(self):
        return(self.__item)
    
    def cargarItem(self,xitem):
        self.__item=xitem

    def cargarSig(self,sig):
        if isinstance(sig,Nodo):
            self.__siguiente=sig
    
    def obtenerSig(self):
        return self.__siguiente

class PilaEncadenada:
    __cant=None
    __tope=None

    def __init__(self,xtope=None,xcant=0) -> None:
        self.__cant=xcant
        self.__tope=xtope
    
    def vacia(self):
        vacia=False
        if self.__tope==None:
            vacia=True
        return vacia
    
    def insertar(self,x):
        nodo=Nodo()
        nodo.cargarItem(x)
        nodo.cargarSig(self.__tope)
        self.__tope=nodo
        self.__cant=self.__cant+1
        return nodo.obtenerItem()

    def suprimir(self):
        x=None
        if self.vacia():
            print('Pila Vacia')
        else:
            x=self.__tope.obtenerItem()
            self.__tope=self.__tope.obtenerSig()
            self.__cant=self.__cant-1
            return x

    def mostrar(self):
        while not self.vacia():
            print(self.suprimir())
    
    def listar(self):
        while not self.vacia():
            print(self.__tope)

