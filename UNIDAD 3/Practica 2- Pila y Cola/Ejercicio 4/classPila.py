import numpy as np #IMPORTAR LOS VECTORES

class PilaSecuencial():
    __items = None
    __topeInf = 0
    __topeSup = 0
    __cant = 0

    def __init__(self,xcant=0):
        self.__items = np.empty(xcant,dtype=int)
        self.__cant = xcant
        self.__topeInf = -1
        self.__topeSup = xcant
    
    def vaciaInf(self):
        vacia = False
        if(self.__topeInf == -1):
            vacia= True
        return vacia
    def vaciaSup(self):
        vacia = False
        if (self.__topeSup == self.__cant):
            vacia = True
        return vacia

    def llena(self):
        llena = False
        if(self.__topeInf == self.__topeSup-1):
            llena = True           
        return llena 

    def insertarInf(self,x):
        llena = self.llena()
        if(not llena):
            self.__topeInf += 1
            self.__items[self.__topeInf] = x    
        else:
            print("Pila inferior llena")

    def insertarSup(self,x):
        llena = self.llena()
        if(not llena):
            self.__topeSup -= 1
            self.__items[self.__topeSup] = x 
        else:
            print("Pila superior llena")

    def suprimirInf(self):
        x = None
        vacia = self.vaciaInf()
        if(vacia):
            x = "Pila inferior vacia"
        else:
            x = self.__items[self.__topeInf]
            self.__topeInf -= 1
        return x

    def suprimirSup(self):
        vacia = self.vaciaSup()
        if(vacia):
            x = "Pila superior vacia"
        else:
            x = self.__items[self.__topeSup]
            self.__topeSup += 1
        return x