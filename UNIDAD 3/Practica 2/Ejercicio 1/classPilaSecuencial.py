class Pila:
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