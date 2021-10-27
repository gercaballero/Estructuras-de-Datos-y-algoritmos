class Nodo:
    __item = None
    __sig = None

    def __init__(self, xitem=0):
        self.__item = xitem
        self.__sig = None

    def setSiguiente(self,sig):
        self.__sig = sig

    def getSiguiente(self):
        return self.__sig

    def getDato(self):
        return self.__dato

class ColaEncadenada:
    __pr = None
    __ul = None
    __cant = 0

    def __init__(self,pr = None, ul = None, xcant = 0):
        self.__pr = pr
        self.__ul = ul
        self.__cant = xcant

    def vacia(self):
        vacia = False
        if self.__cant == 0:
            vacia = True
        return vacia
     
    def insertar(self,x):
        nuevo = Nodo(x)
        if self.__ul == None:
            self.__pr = nuevo
        else:
            self.__ul.setSiguiente(nuevo)
        self.__ul = nuevo
        self.__cant += 1
        return x
    
    def suprimir(self):
        if self.vacia():
            print("Cola vacia")
            return 0
        else:
            x = self.__pr.getDato()
            self.__pr = self.__pr.getSiguiente()
            self.__cant -= 1
            if self.__pr == None: 
                self.__ul = None
            return x