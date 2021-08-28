from classNodo import Nodo
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
