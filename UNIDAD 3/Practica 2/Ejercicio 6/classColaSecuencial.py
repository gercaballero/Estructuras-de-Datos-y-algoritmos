class cola:
    __items=[]
    __max=None
    __pr=None
    __ul=None
    __cant=None
    def __init__(self,xmax=0) -> None:
        self.__pr=0
        self.__ul=0
        self.__cant=0
        self.__max=xmax

    def vacia(self):
        retorna=False
        if self.__cant==0:
            retorna=True
        return retorna
    
    def insertar(self,x):
        if self.__cant<self.__max:
            self.__items[self.__ul]=x
            self.__ul=(self.__ul+1)%self.__max
            self.__cant+=1
            return x
        
    def suprimir(self):
        x=None
        if self.vacia():
            print('PILA VACIA')
            return 0
        else:
            x=self.__items[self.__pr]
            self.__pr=(self.__pr+1)%self.__max
            self.__cant-=1
            return x