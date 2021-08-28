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